import logging

from flask import Flask, render_template, redirect, request, session
from FroRpcReg import *
from FroRpcMan import *
from FroRpcBoo import *
from FroUtils import *
from flask_session import Session


"""
Stato del dizionario quando ritorno dal pagamento
"""
PAGAMENTO_BACK = 5
"""
Stato del dizionario personalizzato quando ritorno dal pagamento
"""
PAGAMENTO_PERSONALIZZATO_BACK = 17
NUM_SEATS = 156
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#logging.basicConfig(filename="application_server.log", level=logging.DEBUG, format=f'%(asctime)s %(message)s')


"""
Pagina Root
"""
@app.route("/")
def menu():
    app.logger.info("Rchiesta pagina root...")
    return render_template("Menu.html")



"""
Gestione dell'iscrizione degli utenti.
"""
@app.route("/iscriviti", methods=('GET','POST'))
def iscrizione():
    
    if request.method == 'POST':
        """
        Estraggo i dati inseriti dall'utente per
        avviare la procedura di iscrizione.
        """
        # Username
        username = request.form['inputUsername']
        # Password
        password = request.form['inputPassword']
        # Conferma password
        passwordConfirm = request.form['inputPasswordConfirm']
        # Email
        email = request.form['inputEmail']
        # Tipologia utente
        userType = request.form['flexRadioDefault']
        # Carta di credito
        cartaDiCredito = request.form['inputCarta']

        #app.logger.info("Richiesta procedura di iscrizione: [" + username + ","+ password + "," + passwordConfirm + "," + email + "," + userType + "]")
        
        """
        Verifico se l'utente che si sta iscrivendo è un
        turista o meno. Se non è un turista, allora sono
        interessato alla compagnia aerea.
        """
        if userType!="Turista":
            """
            Estraggo l'informazine relativa alla
            compagnia aerea inserita.
            """
            airline = request.form['airlineDropdown']
        else:
            """
            Non ho alcun interesse per la compagnia aerea.
            """
            airline = None

        """
        Interazione con il microservizio che gestisce
        le iscrizioni per l'applicazione passandogli
        tutte le informazioni necessarie per completare
        l'iscrizione dell'utente.
        """
        isOk = sendSignUpInfo(email, username, password, passwordConfirm, userType, airline, cartaDiCredito)

        if isOk and userType == "Turista":
            #app.logger.info("Procedura di iscrizione conclusa con successo: [" + username + ","+ password + "," + passwordConfirm + "," + email + "," + userType + "]")
            return redirect('/accedi')
        elif isOk and userType != "Turista":
            #app.logger.info("Procedura di iscrizione conclusa con successo: [" + username + ","+ password + "," + passwordConfirm + "," + email + "," + userType + "," + request.form['airlineDropdown'] + "]")
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
        # Username
        username = request.form['inputUsername']
        # Password
        password = request.form['inputPassword']

        #app.logger.info("Richiesta procedura di accesso: [" + username + ","+ password + "]")

        """
        Verifico le credenziali inserite dall'utente.
        Il campo isCorrect vale TRUE nel momento in
        cui il login ha avuto successo; altrimenri, vale
        FALSE. Il campo storedType contiene il valore
        'Turista' oppure una specifica compagnia aerea.
        """
        response = sendCredentials(username, password)

        #Se le credenziali sono corrette allora si va avanti
        if response.isCorrect == True and response.storedType == "Turista":
            # Salvataggio dello stato della sessione
            session[username] = username
            #app.logger.info("Procedura di accesso completata con successo per l'utente: [" + username + ","+ password + "]")
            return redirect("/"+username+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":
            # Salvataggio dello stato della sessione
            session[response.storedType + username] = response.storedType + username
            #app.logger.info("Procedura di accesso completata con successo per l'utente: [" + username + ","+ password + "," + response.storedType + "]")
            return redirect("/"+response.storedType+"/"+username+"/airlineHome")
        else:
            return render_template("Accesso.html")
    
    #app.logger.warning("Richiesta GET per la procedura di accesso...")
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
        diz = session.pop(username)
        session[username] = username
    except Exception as e:
        """
        Si sta tentando di accedere alla home di un utente
        senza prima aver effettuato correttamente l'accesso.
        """
        return redirect("/accedi", 401)

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
        session.pop(airline + username)
    except:
        """
        Si sta tentando di accedere alla home di un utente
        senza prima aver effettuato correttamente l'accesso.
        """
        return redirect("/accedi", 401)
    
    session[airline + username] = airline + username

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
        if 'cardSelezionata' in keys:
            diz.pop('cardSelezionata')
        if 'bagaglioSpecialePrezzo' in keys:
            diz.pop('bagaglioSpecialePrezzo')
        if 'bagaglioStivaMedioPrezzo' in keys:
            diz.pop('bagaglioStivaMedioPrezzo')
        if 'bagaglioStivaGrandePrezzo' in keys:
            diz.pop('bagaglioStivaGrandePrezzo')
        if 'assicurazioneBagagliPrezzo' in keys:
            diz.pop('assicurazioneBagagliPrezzo')
        if 'animaleDomesticoPrezzo' in keys:
            diz.pop('animaleDomesticoPrezzo')
        if 'neonatoPrezzo' in keys:
            diz.pop('neonatoPrezzo')
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
            #persone = request.form['persone']

            #Non è possibile avere i due aereoporti uguali
            if(partenza == arrivo):
                stringa = "L'AREOPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO\nPROVA AD INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE"
                return render_template("errore.html", errore = stringa)

            """
            Ricavo tutte le informazioni che dovranno essere
            inserite all'interno delle Card da mostrare 
            all'utente che ha richiesto i voli.
            """
            result = sendBookingInfo(giorno, mese, anno, arrivo, partenza)

            """
            Questo pezzo di codice si dovrebbe levare poiché il numero di persone
            viene scelto successivamente...
            for card in result.cards:
                card.prezzoTotale = float(card.prezzoTotale) * float(persone)
            """
            #aggiorno la sessione per questo nuovo utente in modo da portarmi appresso dati necessari per la gestione
            session.pop(username)
            #Mi porto appresso le informazioni relative al numero di persone specficate dall'utente e ai voli che corrispondono alle richieste dell'utente
            session[username] = {'username':username, 'cards':result.cards}

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


@app.route("/<string:username>/<string:compagnia>/<string:idVolo>/resoconto", methods=('GET','POST'))
def resoconto(username, compagnia, idVolo):
    #TODO implementare il resoconto
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
        print("ERRORE 0")
        return redirect("/accedi", 401)

    """
    Non solo devo controllare se esiste la chiave ma devo anche verificare se 
    il dizionario è configurato correttamente per la sessione:
    {'username':value1, 'cards':value3}
    """
    diz = session.get(username)

    if(not isinstance(diz, dict) or (len(diz.keys())!=2 and len(diz.keys())!=5) or diz['username']!=username):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        print("ERRORE 1")
        session.pop(username)
        return redirect("/accedi", 401)


    cardSelezionata = None

    if(len(diz.keys()) == PAGAMENTO_BACK):
        print("SONO TORNATO INDIETRO DA PAGAMENTO!")
        cardSelezionata = diz['cardSelezionata']
        diz.pop('numBigliettiSelezionato')
    else:
        cards = diz['cards']
        check = False
        for card in cards:
            if card.idVolo == idVolo:
                """
                Mi registro il fatto che l'identificativo passato nella URL effettivamente
                corrisponde ad uno dei voli esistenti nello stato della sessione
                """
                check = True
                cardSelezionata = card
                """
                partenza = card.partenza
                arrivo = card.arrivo
                compagnia = card.compagnia
                orario = card.orario
                data = card.data
                prezzoTotale = card.prezzoTotale
                numPosti = card.numPosti
                """

        if(not check):
            """
            Nella URL è stato inserito l'identificativo di un volo insesistente,
            magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
            Faccio la pop per eliminare lo stato della sessione poiché vengo
            reindirizzato all'accesso in cui non ho alcuno stato della sessione.
            """
            print("ERRORE 2")
            session.pop(username)
            return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo e alla card che sono stati selezionati dall'utente
    diz['idVolo'] = idVolo
    diz['cardSelezionata'] = cardSelezionata

    session.pop(username)
    session[username] = diz

    print("[DEBUG SESSIONE (/username/compagnia/idVolo/resoconto)]: key = " + username + "   value = " + str(session.get(username)))
    return render_template("resoconto.html", username = username, card = cardSelezionata)


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

    """
    Ho un numero di chiavi pari a due nel momento in cui provengo
    da booking. Tuttavia, ho un numero di chiavi pari a PAGAMENTO_PERSONALIZZATO_BACK
    se provengo da pagamento personalizzato.
    """
    if(not isinstance(diz, dict) or (len(diz.keys())!=2 and len(diz.keys())!=PAGAMENTO_PERSONALIZZATO_BACK) or diz['username']!=username):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(username)
        return redirect("/accedi", 401)

    """
    Mi porto l'informazione relativa alla card che è stata selezionata dall'utente.
    """
    cardSelezionata = None
    postiDisponibiliVolo = None

    if(len(diz.keys()) == PAGAMENTO_PERSONALIZZATO_BACK):
        print("SONO TORNATO INDIETRO DA PAGAMENTO PERSONALIZZATO!")
        cardSelezionata = diz['cardSelezionata']
        postiDisponibiliVolo = cardSelezionata.posti.posti
        diz.pop('bagaglioSpecialePrezzo')
        diz.pop('bagaglioStivaMedioPrezzo')
        diz.pop('bagaglioStivaGrandePrezzo')
        diz.pop('assicurazioneBagagliPrezzo')
        diz.pop('animaleDomesticoPrezzo')
        diz.pop('neonatoPrezzo')
        diz.pop('bagaglioSpeciale')
        diz.pop('bagaglioStivaMedio')
        diz.pop('bagaglioStivaGrande')
        diz.pop('assicurazioneBagagli')
        diz.pop('animaleDomestico')
        diz.pop('neonato')
        diz.pop('postiSelezionati')
    else:
        cards = diz['cards']
        check = False
        for card in cards:
            if card.idVolo == idVolo:
                """
                Mi registro il fatto che l'identificativo passato nella URL effettivamente
                corrisponde ad uno dei voli esistenti nello stato della sessione
                """
                check = True
                cardSelezionata = card
                postiDisponibiliVolo = card.posti.posti
                """
                partenza = card.partenza
                arrivo = card.arrivo
                compagnia = card.compagnia
                orario = card.orario
                data = card.data
                prezzoTotale = card.prezzoTotale
                numPosti = card.numPosti
                """

        if(not check):
            """
            Nella URL è stato inserito l'identificativo di un volo insesistente,
            magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
            Faccio la pop per eliminare lo stato della sessione poiché vengo
            reindirizzato all'accesso in cui non ho alcuno stato della sessione.
            """
            print("ERRORE 2")
            session.pop(username)
            return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo e alla card che sono stati selezionati dall'utente
    diz['idVolo'] = idVolo
    diz['cardSelezionata'] = cardSelezionata

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

    diz['bagaglioSpecialePrezzo'] = additionalServices.bagaglioSpeciale
    diz['bagaglioStivaMedioPrezzo'] = additionalServices.bagaglioStivaMedio
    diz['bagaglioStivaGrandePrezzo'] = additionalServices.bagaglioStivaGrande
    diz['assicurazioneBagagliPrezzo'] = additionalServices.assicurazioneBagagli
    diz['animaleDomesticoPrezzo'] = additionalServices.animaleDomestico
    diz['neonatoPrezzo'] = additionalServices.neonato
    
    session.pop(username)
    session[username] = diz

    print("[DEBUG SESSION (/username/idVolo/servuzuAggiuntivi)]: key = " + username + "  value = " + str(session.get(username)))    
    return render_template("serviziAggiuntivi.html", username = username, card=cardSelezionata, seatsFlight = seatsFlight, additionalServices = additionalServices, postiDisponibiliVolo = postiDisponibiliVolo)


@app.route("/<string:username>/pagamento", methods=('GET','POST'))
def pagamentoNormale(username):

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

    """
    A questo punto del flusso di esecuzione ci posso arrivare
    SOLAMENTE da normale.html.
    """
    if(not isinstance(diz, dict) or len(diz.keys())!= 5):
        session.pop(username)
        return redirect("/accedi",401)

    #FANFA-NEW
    if request.method == 'POST':

        diz = session.get(username)
        session.pop(username)
        cardSelezionata = diz["cardSelezionata"]
        numBigliettiSelezionato = diz["numBigliettiSelezionato"]

        #la prenotazione può andare a buon fine solo se il volo ha un numero di posti disponibili sufficiente per portare a termine la prenotazione
        if cardSelezionata.numPosti >= numBigliettiSelezionato:
            postiLiberi = cardSelezionata.posti.posti

            #tra le informazioni che ci servono abbiamo già lo username dell'utente racchiuso nella variabile username
            postiPresi = postiLiberi[0:numBigliettiSelezionato]     #i posti che verranno occupati dalla prenotazione
            idVolo = cardSelezionata.idVolo                         #ID del volo prenotato
            dataPagamento = getCurrentDateStr()                     #data del pagamento
            prezzoTotale = int(numBigliettiSelezionato) * int(cardSelezionata.prezzoTotale)    #TODO: cercare di capire 'sta storia dei prezzi
            
            airline = cardSelezionata.compagnia                     #compagnia aerea del volo
            aeroportoPartenza = cardSelezionata.partenza            #aeroporto di partenza
            aeroportoArrivo = cardSelezionata.arrivo                #aeroporto di arrivo
            dataVolo = cardSelezionata.data                         #data del volo
            orarioPartenza = cardSelezionata.orario                 #orario del volo
            email = request.form['user-email']                      #eventuale email immessa dall'utente


            


@app.route("/<string:username>/personalizzato", methods=('GET','POST'))
def pagamentoPersonalizzato(username):

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

    """
    A questo punto del flusso di esecuzione ci posso arrivare
    SOLAMENTE da personalizzato.html.
    """
    if(not isinstance(diz, dict) or len(diz.keys())!= 17):
        session.pop(username)
        return redirect("/accedi",401)

    return render_template("Menu.html")


@app.route("/<string:username>/<string:idVolo>/conferma", methods=('GET','POST'))
def confermaRiepilogo(username, idVolo):
    
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
        numBigliettiSelezionato = request.form['numPosti']
        diz = session.get(username)
        session.pop(username)
        cardSelezionata = diz["cardSelezionata"]
        diz['numBigliettiSelezionato'] = numBigliettiSelezionato
        session[username] = diz
        prezzo_totale = int(numBigliettiSelezionato) * int(cardSelezionata.prezzoTotale)
        print("[DEBUG SESSIONE (/username/idVolo/conferma)]: key = " + username + "   value = " + str(session.get(username)))
        return render_template("normale.html", username = username, card = cardSelezionata, numBigliettiSelezionato = numBigliettiSelezionato, prezzo_totale=prezzo_totale)
    
    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)


@app.route("/<string:username>/<string:idVolo>/personalizzato", methods=('GET','POST'))
def personalizzato(username, idVolo):
    
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
        return redirect("/accedi", 401)

    diz = session.get(username)

    if(not isinstance(diz, dict) or len(diz.keys())!=10 or diz['username']!=username or diz['idVolo']!=idVolo):
        """
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione
        """
        session.pop(username)
        return redirect("/accedi", 401)

    if request.method == 'POST':
        postiSelezionati = request.form.getlist('postiSelezionati')
        bagaglioSpeciale = request.form['Bagaglio speciale']
        bagaglioStivaMedio = request.form['Bagaglio stiva medio']
        bagaglioStivaGrande = request.form['Bagaglio stiva grande']
        assicurazioneBagagli = request.form['assicurazioneBagagli']
        animaleDomestico = request.form['Animale domestico']
        neonato = request.form['Neonato']

        print(postiSelezionati)

        diz = session.get(username)
        session.pop(username)

        diz['postiSelezionati'] = postiSelezionati
        diz['bagaglioSpeciale'] = bagaglioSpeciale
        diz['bagaglioStivaMedio'] = bagaglioStivaMedio
        diz['bagaglioStivaGrande'] = bagaglioStivaGrande
        diz['assicurazioneBagagli'] = assicurazioneBagagli
        diz['animaleDomestico'] = animaleDomestico
        diz['neonato'] = neonato

        session[username] = diz

        prezzo_totale = int(diz['bagaglioSpecialePrezzo'])*int(bagaglioSpeciale) + int(diz['bagaglioStivaMedioPrezzo'])*int(bagaglioStivaMedio) + int(diz['bagaglioStivaGrandePrezzo'])*int(bagaglioStivaGrande) + int(diz['assicurazioneBagagliPrezzo'])*int(assicurazioneBagagli) + int(diz['animaleDomesticoPrezzo'])*int(animaleDomestico) + int(diz['neonatoPrezzo'])*int(neonato)

        print("[DEBUG SESSIONE (/username/idVolo/personalizzato)]: key = " + username + "   value = " + str(session.get(username)))
        
        return render_template("personalizzato.html", prezzoTotale = prezzo_totale, username = username, card = diz['cardSelezionata'])

    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)


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
