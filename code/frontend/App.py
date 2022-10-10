from flask import Flask, render_template, redirect, request, session
from FroRpcReg import *
from FroRpcMan import *
from FroRpcBoo import *
from FroUtils import *
from flask_session import Session

NUM_SEATS = 156

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#very first page
@app.route("/")
def menu():
    return render_template("Menu.html")

#sign in page
@app.route("/accedi", methods=('GET','POST'))
def accesso():
    if request.method == 'POST':
        print("POST")
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        response = sendCredentials(email, password)
        key = response.name+" "+response.surname
        #if credentials are correct then go ahead; else they have to be changed before going to the next page
        if response.isCorrect == True and response.storedType == "Turista":      #tourist case
            session[key] = key
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":    #airline case
            session[response.storedType + key] = response.storedType + key
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")
    return render_template("Accesso.html")
    
@app.route("/<string:fullName>/booking", methods=('GET','POST'))
def booking(fullName):    
    print(session.get(fullName))
    if not session.get(fullName):
        return redirect("/accedi", 302)

    if request.method == 'POST':
        #acquisisco i dati inseriti in input dall'utente
        giorno = request.form['giorno']
        mese = request.form['mese']
        anno = request.form['anno']
        partenza = request.form['aereoporto_partenza']
        arrivo = request.form['aereoporto_arrivo']
        if(partenza == arrivo):
            stringa = "L'AREOPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO\nPROVA AD INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE"
            return render_template("errore.html", errore = stringa)
        persone = request.form['persone']
        result = sendBookingInfo(giorno, mese, anno, partenza, arrivo, persone)
        session.pop(session.get(fullName))
        #Per portarmi avanti l'informazione relativa alle persone'
        session[fullName] = persone
        return render_template("Booking.html", items = result.cards, num = result.num, fullName = fullName)
    return redirect("/accedi")

@app.route("/<string:fullName>/<string:idVolo>/resoconto")
def resoconto(fullName, idVolo):
    #TODO implementare il resoconto
    if not session.get(fullName):
        return redirect("/accedi", 302)
    print("persone = " + session.get(fullName))
    return render_template("resoconto.html")

@app.route("/<string:fullName>/<string:idVolo>/serviziAggiuntivi")
def serviziAggiuntivi(fullName, idVolo):
    #TODO implementare i servizi aggiuntivi
    if not session.get(fullName):
        return redirect("/accedi", 302)
    print("persone = " + session.get(fullName))
    return render_template("serviziAggiuntivi.html")

#logout
@app.route("/<string:fullName>/logout")
def logoutUtentePrenotazione(fullName):
    print(session.get(fullName))
    if not session.get(fullName):
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)
    session.pop(session.get(fullName))
    return redirect("/accedi")

@app.route("/<string:airline>/<string:fullName>/logout")
def logoutUtenteAirline(airline, fullName):
    print(session.get(airline+fullName))
    if not session.get(airline+fullName):
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)
    session.pop(session.get(airline+fullName))
    return redirect("/accedi")


#sign up page
@app.route("/iscriviti", methods=('GET','POST'))
def iscrizione():
    if request.method == 'POST':
        email = request.form['inputEmail']
        name = request.form['inputName']
        surname = request.form['inputSurname']
        password = request.form['inputPassword']
        passwordConfirm = request.form['inputPasswordConfirm']
        userType = request.form['flexRadioDefault']
        airline = request.form['airlineDropdown']

        isOk = sendSignUpInfo(email, name, surname, password, passwordConfirm, userType, airline)

        #if password==passwordConfirm then go ahead; else passwordConfirm has to be changed before going to the next page
        if isOk and userType == "Turista":
            #return redirect("/"+name+" "+surname+"/home")
            return redirect('/accedi')
        elif isOk and userType != "Turista":
            #return redirect("/"+airline+"/"+name+" "+surname+"/airlineHome")
            return redirect('/accedi')
        else:
            return render_template("Iscrizione.html")

    return render_template("Iscrizione.html")

#here the user specifies some information about the flight he wants to book
@app.route("/<string:fullName>/home", methods=('GET','POST'))
def home(fullName):
    if not session.get(session.get(fullName)):
        return redirect("/accedi", 302)
    return render_template("Home.html", fullName=fullName)

#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:fullName>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, fullName):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    return render_template("AirlineHome.html", airline=airline, fullName=fullName)

#here the airline adds a new flight
@app.route("/<string:airline>/<string:fullName>/addFlight", methods=('GET', 'POST'))
def addFlight(airline, fullName):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':

        flightId = request.form['inputId']
        departureAirport = request.form['inputDepartureAirport']
        arrivalAirport = request.form['inputArrivalAirport']
        price = request.form['inputPrice']

        #this function returns a string like "DD-MM-YYYY"
        date = getDate(request.form['dayDropdown'], request.form['monthDropdown'], request.form['yearDropdown'])

        #this function returns a string like "HH:MMAM" or "HH:MMPM"
        fullDepartureHour = getFullHour(request.form['departureHour'], request.form['departureMinute'])
        fullArrivalHour = getFullHour(request.form['arrivalHour'], request.form['arrivalMinute'])

        isOk = sendNewFlight(flightId, date, departureAirport, arrivalAirport, fullDepartureHour, fullArrivalHour, airline, price, NUM_SEATS)

        #if new flight info is ok, then notify the user; else go back to addFlight page because the user has to change something
        if isOk:
            return redirect("/"+airline+"/"+fullName+"/Volo aggiunto")
        else:
            return render_template("AddFlight.html", airline=airline, fullName=fullName)

    return render_template("AddFlight.html", airline=airline, fullName=fullName)

#here the airline modifies the price of an existing flight
@app.route("/<string:airline>/<string:fullName>/modifyFlight", methods=('GET', 'POST'))
def modifyFlight(airline, fullName):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':

        flightId = request.form['inputId']
        newPrice = request.form['inputPrice']

        isOk = sendNewPrice(flightId, newPrice)

        if isOk:
            return redirect("/"+airline+"/"+fullName+"/Prezzi modificati")
        else:
            return render_template("ModifyFlight.html", airline=airline, fullName=fullName)

    return render_template("ModifyFlight.html", airline=airline, fullName=fullName)

#here the airline modifies the price for seat selection
@app.route("/<string:airline>/<string:fullName>/modifySeatsPrices", methods=('GET', 'POST'))
def modifySeatsPrices(airline, fullName):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':

        price1 = request.form['inputPrice1']
        price2 = request.form['inputPrice2']
        price6 = request.form['inputPrice6']
        price16 = request.form['inputPrice16']
        price18 = request.form['inputPrice18']

        isOk = sendSeatsPrices(airline, price1, price2, price6, price16, price18)

        if isOk:
            return redirect("/"+airline+"/"+fullName+"/Prezzi modificati")
        else:
            return render_template("ModifySeatsPrices.html", airline=airline, fullName=fullName)

    return render_template("ModifySeatsPrices.html", airline=airline, fullName=fullName)

#here the airline modifies the price of extra-services
@app.route("/<string:airline>/<string:fullName>/modifyServicesPrices", methods=('GET', 'POST'))
def modifyServicesPrices(airline, fullName):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':

        priceBM = request.form['inputPrice1']
        priceBG = request.form['inputPrice2']
        priceBS = request.form['inputPrice3']
        priceAD = request.form['inputPrice4']
        priceAB = request.form['inputPrice5']
        priceTN = request.form['inputPrice6']

        isOk = sendServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN)

        if isOk:
            return redirect("/"+airline+"/"+fullName+"/Prezzi modificati")
        else:
            return render_template("ModifyServicesPrices.html", airline=airline, fullName=fullName)

    return render_template("ModifyServicesPrices.html", airline=airline, fullName=fullName)

#here an ok message is shown
@app.route("/<string:airline>/<string:fullName>/<string:okMessage>", methods=('GET', 'POST'))
def showOkMessage(airline, fullName, okMessage):
    if not session.get(session.get(airline + fullName)):
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':
        return redirect("/"+airline+"/"+fullName+"/airlineHome")

    return render_template("ManagementOk.html", airline=airline, fullName=fullName, okMessage=okMessage)

if __name__ == "__main__":
    app.run()
