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




"""
Pagina Root
"""
@app.route("/")
def menu():
    return render_template("Menu.html")



"""
Gestione dell'iscrizione degli utenti.
Un utente può essere un Turista o meno.
"""
@app.route("/iscriviti", methods=('GET','POST'))
def iscrizione():
    if request.method == 'POST':
        #Ottengo i dati inseriti dall'utente
        username = request.form['inputUsername']
        password = request.form['inputPassword']
        passwordConfirm = request.form['inputPasswordConfirm']
        email = request.form['inputEmail']
        userType = request.form['flexRadioDefault']

        """
        Verifico se l'utente che si sta iscrivendo è un
        turista o meno. Se non è un turista, allora sono
        interessato anche alla compagnia aerea.
        """
        if userType!="Turista":
            airline = request.form['airlineDropdown']
        else:
            """
            Non ho alcun interesse per la compagnia aerea
            """
            airline = None

        isOk = sendSignUpInfo(email, username, password, passwordConfirm, userType, airline)

        if isOk and userType == "Turista":
            return redirect('/accedi')
        elif isOk and userType != "Turista":
            return redirect('/accedi')
        else:
            return render_template("Iscrizione.html")

    return render_template("Iscrizione.html")




"""
Gestione dell'accesso degli utenti
all'applicazione.
"""
@app.route("/accedi", methods=('GET','POST'))
def accesso():
    if request.method == 'POST':
        #Acquisisco i dati inseriti dall'utente
        username = request.form['inputUsername']
        password = request.form['inputPassword']

        #Verifico le credenziali inserite dall'utente
        response = sendCredentials(username, password)

        #Se le credenziali sono corrette allora si va avanti
        if response.isCorrect == True and response.storedType == "Turista":
            return redirect("/"+username+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":
            return redirect("/"+response.storedType+"/"+username+"/airlineHome")
        else:
            return render_template("Accesso.html")
        
    # Utile nel momento in cui viene eseguita una richiesta GET
    return render_template("Accesso.html")




@app.route("/<string:username>/home", methods=('GET','POST'))
def home(username):
    """
    Questa pop è necessaria poiché è possibile raggiungere la Home
    da parti differenti dell'applicazione e di conseguenza posso
    avere uno stato della sessione differente. Necessito di settare
    il corretto stato della sessione.
    """
    try:
        session.pop(username)
    except Exception as e:
        print(e.args)
        print("[LOG]: l'utente "+username + "si è loggato per la prima volta")

    # Salvataggio dello stato della sessione
    session[username] = username

    print("[DEBUG SESSIONE (/username/home)]: key = " + username + "   value = " + str(session.get(username)))
    return render_template("Home.html", username=username)




#here the airline specifies which information has to be managed
@app.route("/<string:airline>/<string:username>/airlineHome", methods=('GET', 'POST'))
def airlineHome(airline, username):
    """
    Questa pop è necessaria poiché è possibile raggiungere la Home
    da parti differenti dell'applicazione e di conseguenza posso
    avere uno stato della sessione differente. Necessito di settare
    il corretto stato della sessione.
    """
    try:
        session.pop(username)
    except:
        print("[LOG]: l'utente si è loggato per la prima volta")

    session[username] = username

    return render_template("AirlineHome.html", airline=airline, username=username)




@app.route("/<string:username>/booking", methods=('GET','POST'))
def booking(username):
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
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
    diz = session.get(username)
    if(isinstance(diz,dict)):
        keys = diz.keys()
        if 'idVolo' in keys:
            diz.pop('idVolo')
            session.pop(username)
            session[username] = diz
            print("[DEBUG SESSIONE (/username/booking)]: key = " + username + "   value = " + str(session.get(username)))
            return render_template("Booking.html", items = diz['cards'], num = len(diz['cards']), username = username)


    """
    Controllo se i metadati di sessione sono corretti oppure sono alterati.
    Il valore di session.get(username) deve essere uguale a username della URL.
    Anche se un attaccante scrivesse la URL /username/home, senza eseguire l'accesso
    il controllo precedente permetterebbe di bloccarlo.
    """
    if session.get(username) == username:
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
            session.pop(username)
            #Mi porto appresso le informazioni relative al numero di persone specficate dall'utente e ai voli che corrispondono alle richieste dell'utente
            session[username] = {'username':username, 'persone':persone, 'cards':result.cards}

            print("[DEBUG SESSIONE (/username/booking)]: key = " + username + "   value = " + str(session.get(username)))

            #E'necessario portarmi appresso l'informazione relativa al username che mi permette di gestire completamente la sessione
            return render_template("Booking.html", items = result.cards, num = result.num, username = username)
    
        return redirect("/accedi")
    else:
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(username)
        return redirect("/accedi", 401)




@app.route("/<string:username>/<string:idVolo>/pagamento", methods=('GET','POST'))
def confermaRiepilogo(username, idVolo):
    print("[DEBUG SESSIONE (/username/idVolo/pagamento)]: key = " + username + "   value = " + str(session.get(username)))
    
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
        return redirect("/accedi", 401)

    diz = session.get(username)

    if(not isinstance(diz, dict) or len(diz.keys())!=4 or diz['username']!=username or diz['idVolo']!=idVolo):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(username)
        return redirect("/accedi", 401)    

    if request.method == 'POST':
        return render_template("pagamento.html", username = username)
    
    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)



@app.route("/<string:username>/<string:compagnia>/<string:idVolo>/resoconto")
def resoconto(username, compagnia, idVolo):
    #TODO implementare il resoconto
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
        return redirect("/accedi", 401)

    """
    Non solo devo controllare se esiste la chiave ma devo anche verificare se 
    il dizionario è configurato correttamente per la sessione:
    {'username':value1, 'persone':value2, 'cards':value3}
    """
    diz = session.get(username)

    if(not isinstance(diz, dict) or len(diz.keys())!=3 or diz['username']!=username):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(username)
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
        session.pop(username)
        return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo che è stato selezionato dall'utente
    diz['idVolo'] = idVolo
    session.pop(username)
    session[username] = diz
    print("[DEBUG SESSIONE (/username/compagnia/idVolo/resoconto)]: key = " + username + "   value = " + str(session.get(username)))
    return render_template("resoconto.html", username = username, idVolo = idVolo, arrivo = arrivo, partenza = partenza, compagnia = compagnia, orario = orario, data = data, prezzoTotale = prezzoTotale)




@app.route("/<string:username>/<string:compagnia>/<string:idVolo>/serviziAggiuntivi")
def serviziAggiuntivi(username, compagnia, idVolo):
    """
    Arrivato a questo punto, devo avere uno stato differente da None.
    """
    if session.get(username) is None:
        return redirect("/accedi", 401)

    """
    Non solo devo controllare se esiste la sessione relativa a
    tale utente, ma devo anche verificare se il dizionario è
    configurato correttamente per la sessione corrente.
    """
    diz = session.get(username)

    if(not isinstance(diz, dict) or len(diz.keys())!=3 or diz['username']!=username):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(username)
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
        session.pop(username)
        return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo che è stato selezionato dall'utente
    diz['idVolo'] = idVolo
    session.pop(username)
    session[username] = diz

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

    print("[DEBUG SESSION (/username/idVolo/servuzuAggiuntivi)]: key = " + username + "  value = " + str(session.get(username)))    
    return render_template("serviziAggiuntivi.html", username = username, seatsFlight = seatsFlight, additionalServices = additionalServices, postiDisponibiliVolo = postiDisponibiliVolo)



#logout
@app.route("/<string:username>/logout")
def logoutUtentePrenotazione(username):
    if session.get(username) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)

    # Termino la sessione relativa all'utente loggato
    session.pop(username)

    return redirect("/accedi")



@app.route("/<string:airline>/<string:username>/logout")
def logoutUtenteAirline(airline, username):
    print(session.get(airline+username))
    #if not session.get(airline+username):
    if session.get(airline+username) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE"
        return render_template("errore.html", errore = stringa)
    #session.pop(session.get(airline+username))
    session.pop(airline+username)
    return redirect("/accedi")




#here the airline adds a new flight
@app.route("/<string:airline>/<string:username>/addFlight", methods=('GET', 'POST'))
def addFlight(airline, username):
    #if not session.get(session.get(airline + username)):
    if session.get(airline + username) is None:
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
            return redirect("/"+airline+"/"+username+"/Volo aggiunto")
        else:
            return render_template("AddFlight.html", airline=airline, username=username)

    return render_template("AddFlight.html", airline=airline, username=username)



#here the airline modifies the price of an existing flight
@app.route("/<string:airline>/<string:username>/modifyFlight", methods=('GET', 'POST'))
def modifyFlight(airline, username):
    #if not session.get(session.get(airline + username)):
    if session.get(airline + username) is None:
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':

        flightId = request.form['inputId']
        newPrice = request.form['inputPrice']

        isOk = sendNewPrice(flightId, newPrice)

        if isOk:
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("ModifyFlight.html", airline=airline, username=username)

    return render_template("ModifyFlight.html", airline=airline, username=username)



#here the airline modifies the price for seat selection
@app.route("/<string:airline>/<string:username>/modifySeatsPrices", methods=('GET', 'POST'))
def modifySeatsPrices(airline, username):
    #if not session.get(session.get(airline + username)):
    if session.get(airline + username) is None:
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
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("ModifySeatsPrices.html", airline=airline, username=username)

    return render_template("ModifySeatsPrices.html", airline=airline, username=username)



#here the airline modifies the price of extra-services
@app.route("/<string:airline>/<string:username>/modifyServicesPrices", methods=('GET', 'POST'))
def modifyServicesPrices(airline, username):
    #if not session.get(session.get(airline + username)):
    if session.get(airline + username) is None:
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
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("ModifyServicesPrices.html", airline=airline, username=username)

    return render_template("ModifyServicesPrices.html", airline=airline, username=username)



#here an ok message is shown
@app.route("/<string:airline>/<string:username>/<string:okMessage>", methods=('GET', 'POST'))
def showOkMessage(airline, username, okMessage):
    #if not session.get(session.get(airline + username)):
    if session.get(airline + username) is None:
        print("Dentro")
        return redirect("/accedi", 302)
    if request.method == 'POST':
        return redirect("/"+airline+"/"+username+"/airlineHome")

    return render_template("ManagementOk.html", airline=airline, username=username, okMessage=okMessage)



if __name__ == "__main__":
    app.run()
