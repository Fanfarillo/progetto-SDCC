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
            return redirect("/"+response.name+" "+response.surname+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":
            return redirect("/"+response.storedType+"/"+response.name+" "+response.surname+"/airlineHome")
        else:
            return render_template("Accesso.html")
        
    # Utile nel momento in cui viene eseguita una richiesta GET
    return render_template("Accesso.html")




@app.route("/<string:fullName>/booking", methods=('GET','POST'))
def booking(fullName):
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(fullName) is None:
        return redirect("/accedi", 401)

    """
    E' possibile arrivare a questo punto anche premendo
    il tasto indietro da pagine html differenti dopo aver
    selezionato un volo. Di conseguenza, è necessario cambiare
    lo stato della sessione cancellando l'informazione relativa
    al volo che è stato selezionato in precedenza dall'utente.
    In questo punto dell'applicazione, l'utente deve scegliere
    nuovamente il volo.
    """
    diz = session.get(fullName)
    if(isinstance(diz,dict)):
        keys = diz.keys()
        if 'idVolo' in keys:
            diz.pop('idVolo')
            session.pop(fullName)
            session[fullName] = diz
            print("[DEBUG SESSIONE (/fullName/booking)]: key = " + fullName + "   value = " + str(session.get(fullName)))
            return render_template("Booking.html", items = diz['cards'], num = len(diz['cards']), fullName = fullName)


    """
    Controllo se i metadati di sessione sono corretti oppure sono alterati.
    Il valore di session.get(fullName) deve essere uguale a fullName della URL.
    Anche se un attaccante scrivesse la URL /fullName/home, senza eseguire l'accesso
    il controllo precedente permetterebbe di bloccarlo.
    """
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

            for card in result.cards:
                """
                Dal microservizio ottengo il prezzo a persona per il biglietto.
                Di conseguenza, necessito di eseguire questa moltiplicazione per
                ottenere il PREZZO TOTALE.
                """
                card.prezzoTotale = float(card.prezzoTotale) * float(persone)

            #aggiorno la sessione per questo nuovo utente in modo da portarmi appresso dati necessari per la gestione
            session.pop(fullName)
            #Mi porto appresso le informazioni relative al numero di persone specficate dall'utente e ai voli che corrispondono alle richieste dell'utente
            session[fullName] = {'fullName':fullName, 'persone':persone, 'cards':result.cards}

            print("[DEBUG SESSIONE (/fullName/booking)]: key = " + fullName + "   value = " + str(session.get(fullName)))

            #E'necessario portarmi appresso l'informazione relativa al fullName che mi permette di gestire completamente la sessione
            return render_template("Booking.html", items = result.cards, num = result.num, fullName = fullName)
    
        return redirect("/accedi")
    else:
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(fullName)
        return redirect("/accedi", 401)



#@app.route("/<string:fullName>/<string:idVolo/pagamento", methods=('GET','POST'))
@app.route("/<string:fullName>/<string:idVolo>/pagamento", methods=('GET','POST'))
def confermaRiepilogo(fullName, idVolo):
    print("[DEBUG SESSIONE (/fullName/idVolo/pagamento)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(fullName) is None:
        return redirect("/accedi", 401)

    diz = session.get(fullName)

    if(not isinstance(diz, dict) or len(diz.keys())!=4 or diz['fullName']!=fullName or diz['idVolo']!=idVolo):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(fullName)
        return redirect("/accedi", 401)    

    if request.method == 'POST':
        return render_template("pagamento.html", fullName = fullName)
    
    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)



@app.route("/<string:fullName>/<string:compagnia>/<string:idVolo>/resoconto")
def resoconto(fullName, compagnia, idVolo):
    #TODO implementare il resoconto
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(fullName) is None:
        return redirect("/accedi", 401)

    """
    Non solo devo controllare se esiste la chiave ma devo anche verificare se 
    il dizionario è configurato correttamente per la sessione:
    {'fullName':value1, 'persone':value2, 'cards':value3}
    """
    diz = session.get(fullName)

    if(not isinstance(diz, dict) or len(diz.keys())!=3 or diz['fullName']!=fullName):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(fullName)
        return redirect("/accedi", 401)

    cards = diz['cards']
    check = False

    for card in cards:
        if card.idVolo == idVolo:
            """
            Mi registro il fatto che l'identificativo passato nella URL effettivamente
            corrisponde ad uno dei voli esistenti nello stato della sessione
            """
            check = True

            partenza = card.partenza
            arrivo = card.arrivo
            compagnia = card.compagnia
            orario = card.orario
            data = card.data
            prezzoTotale = card.prezzoTotale

    if(not check):
        """
        Nella URL è stato inserito l'identificativo di un volo insesistente,
        magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(fullName)
        return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo che è stato selezionato dall'utente
    diz['idVolo'] = idVolo
    session.pop(fullName)
    session[fullName] = diz
    print("[DEBUG SESSIONE (/fullName/compagnia/idVolo/resoconto)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    return render_template("resoconto.html", fullName = fullName, idVolo = idVolo, arrivo = arrivo, partenza = partenza, compagnia = compagnia, orario = orario, data = data, prezzoTotale = prezzoTotale)



@app.route("/<string:fullName>/<string:compagnia>/<string:idVolo>/serviziAggiuntivi")
def serviziAggiuntivi(fullName, compagnia, idVolo):
    """
    Arrivato a questo punto, devo avere uno stato differente da None.
    """
    if session.get(fullName) is None:
        return redirect("/accedi", 401)

    """
    Non solo devo controllare se esiste la sessione relativa a
    tale utente, ma devo anche verificare se il dizionario è
    configurato correttamente per la sessione corrente.
    """
    diz = session.get(fullName)

    if(not isinstance(diz, dict) or len(diz.keys())!=3 or diz['fullName']!=fullName):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(fullName)
        return redirect("/accedi", 401)

    cards = diz['cards']

    #Per vedere se l'identificativo del volo selezionato sta tra le possibili scelte dell'utente
    check = False
    for card in cards:
        if card.idVolo == idVolo:
            """
            Mi registro il fatto che l'identificativo passato nella URL effettivamente
            corrisponde ad uno dei voli esistenti nello stato della sessione
            """
            check = True
            postiDisponibiliVolo = card.posti.posti

    if(not check):
        """
        Nella URL è stato inserito l'identificativo di un volo insesistente,
        magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(fullName)
        return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo che è stato selezionato dall'utente
    diz['idVolo'] = idVolo
    session.pop(fullName)
    session[fullName] = diz

    #TODO metti un controllo su quanti sono i posti disponibili

    #Ottengo il costo dei posti della compagnia aerea in questione
    seatsFlight = sendIdCompanySeatsPrice(compagnia)
    print("[1]: " + str(seatsFlight.primo))
    print("[2-5]: " + str(seatsFlight.secondo))
    print("[6-15]: " + str(seatsFlight.terzo))
    print("[16-17]: " + str(seatsFlight.quarto))
    print("[18-26]: " + str(seatsFlight.quinto))

    #Ottengo il costo dei servizi aggiuntivi della compagnia aerea in questione
    additionalServices = sendIdCompanydditionalService(compagnia)
    print("bagaglioSpeciale: " + str(additionalServices.bagaglioSpeciale))
    print("bagaglioStivaMedio: " + str(additionalServices.bagaglioStivaMedio))
    print("bagaglioStivaGrande: " + str(additionalServices.bagaglioStivaGrande))
    print("assicurazioneBagagli: " + str(additionalServices.assicurazioneBagagli))
    print("animaleDomestico: " + str(additionalServices.animaleDomestico))
    print("neonato: " + str(additionalServices.neonato))

    print("[DEBUG SESSION (/fullName/idVolo/servuzuAggiuntivi)]: key = " + fullName + "  value = " + str(session.get(fullName)))    
    return render_template("serviziAggiuntivi.html", fullName = fullName, seatsFlight = seatsFlight, additionalServices = additionalServices, postiDisponibiliVolo = postiDisponibiliVolo)



#logout
@app.route("/<string:fullName>/logout")
def logoutUtentePrenotazione(fullName):
    if session.get(fullName) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)

    # Termino la sessione relativa all'utente loggato
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
        #Ottengo i dati inseriti dall'utente
        email = request.form['inputEmail']
        name = request.form['inputName']
        surname = request.form['inputSurname']
        password = request.form['inputPassword']
        passwordConfirm = request.form['inputPasswordConfirm']
        userType = request.form['flexRadioDefault']

        """
        Verifico se l'utente che si sta iscrivendo è un
        turista o meno. Se non è un turista, allora sono
        interessato anche alla compagnia aerea.
        """
        if userType!="Turista":
            airline = request.form['airlineDropdown']
        else:
            airline = None
        isOk = sendSignUpInfo(email, name, surname, password, passwordConfirm, userType, airline)

        if isOk and userType == "Turista":
            return redirect('/accedi')
        elif isOk and userType != "Turista":
            return redirect('/accedi')
        else:
            return render_template("Iscrizione.html")

    return render_template("Iscrizione.html")




@app.route("/<string:fullName>/home", methods=('GET','POST'))
def home(fullName):
    """
    Questa pop è necessaria poiché è possibile raggiungere la Home
    da parti differenti dell'applicazione e di conseguenza posso
    avere uno stato della sessione differente. Necessito di settare
    il corretto stato della sessione.
    """
    try:
        session.pop(fullName)
    except:
        print("[LOG]: l'utente "+fullName + "si è loggato per la prima volta")

    # Salvataggio dello stato della sessione
    session[fullName] = fullName

    print("[DEBUG SESSIONE (/fullName/home)]: key = " + fullName + "   value = " + str(session.get(fullName)))
    return render_template("Home.html", fullName=fullName)




#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:fullName>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, fullName):
    """
    Questa pop è necessaria poiché è possibile raggiungere la Home
    da parti differenti dell'applicazione e di conseguenza posso
    avere uno stato della sessione differente. Necessito di settare
    il corretto stato della sessione.
    """
    try:
        session.pop(fullName)
    except:
        print("[LOG]: l'utente si è loggato per la prima volta")

    session[fullName] = fullName

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
