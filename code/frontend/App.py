from flask import Flask, render_template, redirect, request, session #nuovo
from FroRpcReg import *
from FroRpcMan import *
from FroRpcBoo import *
from FroUtils import *
from flask_session import Session #nuovo

NUM_SEATS = 156

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False #nuovo
app.config["SESSION_TYPE"] = "filesystem"   #nuovo
Session(app)    #nuovo


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
        #print(key)
        session[key] = key
        #print(session.get(key))
        #if credentials are correct then go ahead; else they have to be changed before going to the next page
        if response.isCorrect == True and response.storedType == "Turista":      #tourist case
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":    #airline case
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")
    print("GET")
    return render_template("Accesso.html")
    
@app.route("/booking", methods=('GET','POST'))
def booking():
    
    print(session.get(request.form.get("fullName")))
    if not session.get(request.form.get("fullName")):
        print("Dentro")
        return redirect("/accedi", 302)
    print("Fuori")

    if request.method == 'POST':
        #acquisisco i dati inseriti in input dall'utente
        giorno = request.form['giorno']
        print(giorno)
        mese = request.form['mese']
        print(mese)
        anno = request.form['anno']
        print(anno)
        partenza = request.form['aereoporto_partenza']
        print(partenza)
        arrivo = request.form['aereoporto_arrivo']
        print(arrivo)
        if(partenza == arrivo):
            stringa = "L'AREOPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO\nPROVA AD INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE"
            return render_template("errorePrenotazione.html", errore = stringa)
        persone = request.form['persone']
        print(persone)
        cards = sendBookingInfo(giorno, mese, anno, partenza, arrivo, persone)
        print(len(cards))
        return render_template("Booking.html", items = cards)
    return render_template("Accesso.html")

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
            return redirect("/"+name+" "+surname+"/home")
        elif isOk and userType != "Turista":
            return redirect("/"+airline+"/"+name+" "+surname+"/airlineHome")
        else:
            return render_template("Iscrizione.html")

    return render_template("Iscrizione.html")

#here the user specifies some information about the flight he wants to book
@app.route("/<string:fullName>/home", methods=('GET','POST'))
def home(fullName):
    """print(session.get(request.form.get(fullName)))
    if not session.get(request.form.get(fullName)):
        print("Dentro")
        return redirect("/accedi", 302)"""
    print("Fuori")
    return render_template("Home.html", fullName=fullName)

#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:fullName>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, fullName):
    return render_template("AirlineHome.html", airline=airline, fullName=fullName)

#here the airline adds a new flight
@app.route("/<string:airline>/<string:fullName>/addFlight", methods=('GET', 'POST'))
def addFlight(airline, fullName):
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
    if request.method == 'POST':
        return redirect("/"+airline+"/"+fullName+"/airlineHome")

    return render_template("ManagementOk.html", airline=airline, fullName=fullName, okMessage=okMessage)

if __name__ == "__main__":
    app.run()
