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
        #Acquisisco i dati inseriti dall'utente
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        #Verifico le credenziali inserite dall'utente
        response = sendCredentials(email, password)
        fullName = response.name+" "+response.surname

        #Se le credenziali sono corrette allora si va avanti
        if response.isCorrect == True and response.storedType == "Turista":
            session[fullName] = fullName
            print("[DEBUG SESSIONE (/accedi)]: key = " + fullName + "   value = " + str(session.get(fullName)))
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":
            session[response.storedType + fullName] = response.storedType + fullName
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")
        
    #Utile nel momento in cui viene eseguita una richiesta GET
    return render_template("Accesso.html")



@app.route("/<string:fullName>/booking", methods=('GET','POST'))
def booking(fullName):

    #sessione.get(fullName) = fullName se la richiesta è valida; altrimenti, vale None
    if session.get(fullName) is None:
        return redirect("/accedi", 302)

    keys = session.get(fullName).keys()

    #Controllo se i metadati di sessione sono corretti oppure sono alterati
    if session.get(fullName) == fullName:
        if request.method == 'POST':
            #acquisisco i dati inseriti in input dall'utente
            giorno = request.form['giorno']
            mese = request.form['mese']
            anno = request.form['anno']
            partenza = request.form['aereoporto_partenza']
            arrivo = request.form['aereoporto_arrivo']
            persone = request.form['persone']

            #Non è possibile avere i due aereoporti uguali
            if(partenza == arrivo):
                stringa = "L'AREOPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO\nPROVA AD INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE"
                return render_template("errore.html", errore = stringa)

            result = sendBookingInfo(giorno, mese, anno, arrivo, partenza, persone)
            #aggiorno la sessione per questo nuovo utente in modo da portarmi appresso dati necessari per la gestione
            session.pop(fullName)
            #Mi porto appresso le informazioni relative al numero di persone specficate dall'utente e ai voli che corrispondono alle richieste dell'utente
            session[fullName] = {'fullName':fullName, 'persone':persone, 'cards':result.cards}
            for card in result.cards:
                #Dal microservizio ottenfo il prezzo a persona per il biglietto
                #Di conseguenza, necessito di eseguire questa moltiplicazione per ottenere il PREZZO TOTALE
                card.prezzoTotale = float(card.prezzoTotale) * float(persone)
            #E'necessario portarmi appresso l'informazione relativa al fullName che mi permette di gestire completamente la sessione
            print("[DEBUG SESSIONE (/fullName/booking)]: key = " + fullName + "   value = " + str(session.get(fullName)))
            return render_template("Booking.html", items = result.cards, num = result.num, fullName = fullName)
    
        return redirect("/accedi")
    else:
        session.pop(fullName)
        redirect("/accedi")



#@app.route("/<string:fullName>/<string:idVolo/pagamento", methods=('GET','POST'))
@app.route("/<string:fullName>/pagamento", methods=('GET','POST'))
def confermaRiepilogo(fullName):
    print("[DEBUG SESSIONE (/fullName/pagamento)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    #if not session.get(fullName):
    if session.get(fullName) is None:
        return redirect("/accedi", 302)
    if request.method == 'POST':
        return render_template("pagamento.html", fullName = fullName)
    
    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)



@app.route("/<string:fullName>/<string:idVolo>/resoconto")
def resoconto(fullName, idVolo):
    #TODO implementare il resoconto

    #if not session.get(fullName):
    if session.get(fullName) is None:
        return redirect("/accedi", 302)

    #Non solo devo controllare se esiste la chiave ma devo anche verificare se il dizionario è configurato correttamente
    diz = session.get(fullName)
    if(not isinstance(diz, dict) || len(diz.keys())!=3 or diz['fullName'!=fullName or diz['idVolo']!=idVolo):
        session.pop(fullName)
        return redirect("/accedi")

    cards = diz['cards']
    check = False

    for card in cards:
        if card.idVolo == idVolo:
            #Mi registro il fatto che l'identificativo passato nella URL effettivamente corrisponde ad uno dei voli esistenti
            check = True
            partenza = card.partenza
            print("PARTENZA= ", card.partenza)
            arrivo = card.arrivo
            print("ARRIVO= ", card.arrivo)
            compagnia = card.compagnia
            print("PARTENZA= ", card.compagnia)
            orario = card.orario
            print("PARTENZA= ", card.orario)
            data = card.data
            print("PARTENZA= ", card.data)
            prezzoTotale = card.prezzoTotale
            print("PARTENZA= ", card.prezzoTotale) 

    if(not check):
        #Nella URL è stato inserito l'identificativo di un volo insesistente, magari per sbaglio da parte dell'utente oppure come tentativo di attacco
        session.pop(fullName)
        """
        Modifico i metadati di sessione che mi porto appresso ritornando al valore che la sessione ha nel momento in cui sono alla Home
        Quindi non ho più le informazioni relative alle persone, ai risultati della ricerca e all'identificativo del volo che ho scelto
        """
        session[fullName] = fullName
        return redirect("/"+fullName+"/home", 302)

    #Mi porto appresso anche le informazioni relative al volo che è stato selezionato dall'utente
    diz['idVolo'] = idVolo
    session.pop(fullName)
    session[fullName] = diz
    print("[DEBUG SESSIONE (/fullName/home)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    return render_template("resoconto.html", fullName = fullName, idVolo = idVolo, arrivo = arrivo, partenza = partenza, compagnia = compagnia, orario = orario, data = data, prezzoTotale = prezzoTotale)



@app.route("/<string:fullName>/<string:idVolo>/serviziAggiuntivi")
def serviziAggiuntivi(fullName, idVolo):
    #TODO implementare i servizi aggiuntivi
    #if not session.get(fullName):
    if session.get(fullName) is None:
        return redirect("/accedi", 302)
    print("persone = " + session.get(fullName))
    return render_template("serviziAggiuntivi.html")



#logout
@app.route("/<string:fullName>/logout")
def logoutUtentePrenotazione(fullName):
    #print(session.get(fullName))
    #if not session.get(fullName):
    print("sono qua: ",session.get(fullName))
    if session.get(fullName) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)
    #session.pop(session.get(fullName))
    session.pop(fullName)
    return redirect("/accedi")



@app.route("/<string:airline>/<string:fullName>/logout")
def logoutUtenteAirline(airline, fullName):
    print(session.get(airline+fullName))
    #if not session.get(airline+fullName):
    if session.get(airline+fullName) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)
    #session.pop(session.get(airline+fullName))
    session.pop(airline+fullName)
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
    #if not session.get(session.get(fullName)):
    print("[DEBUG SESSIONE (/fullName/home)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    if (session.get(fullName) is None) or (session.get(fullName)!=fullName):
        return redirect("/accedi", 302)
    return render_template("Home.html", fullName=fullName)



#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:fullName>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, fullName):
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
        print("Dentro")
        return redirect("/accedi", 302)
    return render_template("AirlineHome.html", airline=airline, fullName=fullName)



#here the airline adds a new flight
@app.route("/<string:airline>/<string:fullName>/addFlight", methods=('GET', 'POST'))
def addFlight(airline, fullName):
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
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
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
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
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
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
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
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
    #if not session.get(session.get(airline + fullName)):
    if session.get(airline + fullName) is None:
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':
        return redirect("/"+airline+"/"+fullName+"/airlineHome")

    return render_template("ManagementOk.html", airline=airline, fullName=fullName, okMessage=okMessage)



if __name__ == "__main__":
    app.run()
