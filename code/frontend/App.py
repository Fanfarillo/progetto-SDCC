from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from decimal import *

from FroRpcReg import *
from FroRpcMan import *
from FroRpcBoo import *
from FroRpcPay import *
from FroRpcSug import *
from FroUtils import *


PAGAMENTO_BACK = 5                      # Stato del dizionario quando ritorno dal pagamento
PAGAMENTO_PERSONALIZZATO_BACK = 12      # Stato del dizionario personalizzato quando ritorno dal pagamento
NUM_SEATS = 156                         # Numero di posti disponibili per il volo

app = Flask(__name__)
app.debug = True
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
        # Tipologia utente
        userType = request.form['flexRadioDefault']
        # Carta di credito
        cartaDiCredito = request.form['inputCarta']
        
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
        response = sendSignUpInfo(username, password, passwordConfirm, userType, airline, cartaDiCredito)

        if response.isOk:
            # L'iscrizione è stata completata con successo.
            return redirect('/accedi')
        else:
            # L'iscrizion non è stata completata con successo.
            return render_template("errore.html", errore=response.error, airline=None, username=None)

    return render_template("Iscrizione.html")




"""
Gestione dell'accesso degli utenti
all'applicazione.
"""
@app.route("/accedi", methods=('GET','POST'))
def accesso():

    if request.method == 'POST':

        """
        Ottengo le credenziali inserite dall'utente
        per richiedere il Login al sistema.
        """
        # Username
        username = request.form['inputUsername']
        # Password
        password = request.form['inputPassword']


        """
        Verifico le credenziali inserite dall'utente.
        Il campo isCorrect vale TRUE nel momento in
        cui il login ha avuto successo; altrimenti, vale
        FALSE. Il campo storedType contiene il valore
        'Turista' oppure una specifica compagnia aerea.
        """
        response = sendCredentials(username, password)

        #Se le credenziali sono corrette allora si va avanti
        if response.isCorrect == True and response.storedType == "Turista":
            # Salvataggio dello stato della sessione
            session[username] = username
            return redirect("/"+username+"/home")
        elif response.isCorrect == True and response.storedType != "Turista":
            # Salvataggio dello stato della sessione
            session[response.storedType + username] = response.storedType + username
            return redirect("/"+response.storedType+"/"+username+"/airlineHome")
        else:
            stringa = "LE CREDENZIALI IMMESSE SONO ERRATE.\nPROVA AD ACCEDERE NUOVAMENTE."
            return render_template("errore.html", errore=stringa, airline=None, username=None)
    
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
        Infatti, non si ha alcuna sessione relativa al valore
        di username.
        """
        return redirect("/accedi", 401)

    #qui è necessario fare una query a Booking per recuperare gli aeroporti da inserire nelle scrollbar "Aeroporto di partenza" e "Aeroporto di destinazione"
    airportsLists = retrieveAirports()

    print("[DEBUG SESSIONE (/username/home)]: key = " + username + "   value = " + str(session.get(username)))
    return render_template("Home.html", username=username, airportsLists=airportsLists)




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
        Infatti, non si ha alcuna sessione relativa al valore
        di airline + username.
        """
        return redirect("/accedi", 401)
    
    session[airline + username] = airline + username

    return render_template("AirlineHome.html", airline=airline, username=username)




@app.route("/<string:username>/booking", methods=('GET','POST'))
def booking(username):
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    poiché l'utente deve aver fatto il Login e inserito dei dati.
    """
    if session.get(username) is None:
        return redirect("/accedi", 401)

    """
    E' possibile arrivare a questo punto anche premendo
    il tasto 'indietro' da pagine html differenti dopo aver
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
        if 'prezziFilePosti' in keys:
            diz.pop('prezziFilePosti')
        if 'prezziServizi' in keys:
            diz.pop('prezziServizi')

        session.pop(username)
        session[username] = diz

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
            partenza = request.form['aeroporto_partenza']
            arrivo = request.form['aeroporto_arrivo']

            #this function returns a string like "DD-MM-YYYY"
            date = getDate(giorno, mese, anno)

            #non è possibile avere gli aeroporti non selezionati
            """
            if partenza=="Selezionare un aeroporto" or arrivo=="Selezionare un aeroporto":
                stringa = "È NECESSARIO SELEZIONARE GLI AEROPORTI DI PARTENZA E DI ARRIVO.\nPROVA A INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE."
                return render_template("errore.html", errore=stringa, airline=None, username=username)
            """

            #sanity checks are the following:
            #   1) Date should exist (e.g. it cannot be '31-04-2023')
            #   2) Date should be future
            #   3) Departure airport != arrival airport
            isExistentDate = checkDateExistance(date)         #condition 1)
            if isExistentDate:
                isFutureDate = checkFutureDate(date)          #condition 2)

            if not isExistentDate:
                stringa = "LA DATA INSERITA NON ESISTE.\nPROVA A INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE."
                return render_template("errore.html", errore=stringa, airline=None, username=username)
            elif not isFutureDate:
                stringa = "LA DATA INSERITA DEVE ESSERE SUCCESSIVA A QUELLA ODIERNA.\nPROVA A INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE."
                return render_template("errore.html", errore=stringa, airline=None, username=username)
            elif partenza == arrivo:                          #condition 3)
                stringa = "L'AEROPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO.\nPROVA A INSERIRE NUOVAMENTE I DATI DELLA PRENOTAZIONE."
                return render_template("errore.html", errore=stringa, airline=None, username=username)

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
                card.prezzoBase = float(card.prezzoBase) * float(persone)
            """
            #aggiorno la sessione per questo nuovo utente in modo da portarmi appresso dati necessari per la gestione
            session.pop(username)
            #Mi porto appresso le informazioni relative al numero di persone specficate dall'utente e ai voli che corrispondono alle richieste dell'utente
            session[username] = {'username':username, 'cards':result.cards}

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
    """
    Arrivato a questo punto, devo avere uno stato differente da None
    """
    if session.get(username) is None:
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
        session.pop(username)
        return redirect("/accedi", 401)


    cardSelezionata = None

    if(len(diz.keys()) == PAGAMENTO_BACK):
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
                prezzoBase = card.prezzoBase
                numPosti = card.numPosti
                """

        if(not check):
            """
            Nella URL è stato inserito l'identificativo di un volo insesistente,
            magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
            Faccio la pop per eliminare lo stato della sessione poiché vengo
            reindirizzato all'accesso in cui non ho alcuno stato della sessione.
            """
            session.pop(username)
            return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo e alla card che sono stati selezionati dall'utente
    diz['idVolo'] = idVolo
    diz['cardSelezionata'] = cardSelezionata

    session.pop(username)
    session[username] = diz

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
        cardSelezionata = diz['cardSelezionata']
        postiDisponibiliVolo = cardSelezionata.posti.posti
        diz.pop('postiSelezionati')
        diz.pop('serviziSelezionati')
        diz.pop('numBigliettiAcquistati')
        diz.pop('prezzoSelezionePosti')
        diz.pop('prezzoServiziAggiuntivi')
        diz.pop('prezzoTotale')
        diz.pop('prezziFilePosti')
        diz.pop('prezziServizi')

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

        if(not check):
            """
            Nella URL è stato inserito l'identificativo di un volo insesistente,
            magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
            Faccio la pop per eliminare lo stato della sessione poiché vengo
            reindirizzato all'accesso in cui non ho alcuno stato della sessione.
            """
            session.pop(username)
            return redirect("/accedi", 401)

    #Mi porto appresso anche le informazioni relative al volo e alla card che sono stati selezionati dall'utente
    diz['idVolo'] = idVolo
    diz['cardSelezionata'] = cardSelezionata

    #Ottengo il costo dei posti della compagnia aerea in questione
    seatsFlight = sendIdCompanySeatsPrice(compagnia)
    #I prezzi per la selezione dei posti verranno inseriti all'interno della sessione ma raggruppati nell'oggetto Python per motivi di compattezza
    diz['prezziFilePosti'] = seatsFlight

    #Ottengo il costo dei servizi aggiuntivi della compagnia aerea in questione
    additionalServices = sendIdCompanyAdditionalService(compagnia)
    #Anche i prezzi per i servizi aggiuntivi verranno inseriti all'interno della sessione ma raggruppati in un oggetto Python per motivi di compattezza
    diz['prezziServizi'] = additionalServices
   
    session.pop(username)
    session[username] = diz

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

    if request.method == 'POST':

        diz = session.get(username)
        session.pop(username)
        cardSelezionata = diz["cardSelezionata"]
        numBigliettiSelezionato = diz["numBigliettiSelezionato"]
        session[username] = diz

        #la prenotazione può andare a buon fine solo se il volo ha un numero di posti disponibili sufficiente per portare a termine la prenotazione
        if cardSelezionata.numPosti >= numBigliettiSelezionato:
            postiLiberi = cardSelezionata.posti.posti

            #tra le informazioni che ci servono abbiamo già lo username dell'utente racchiuso nella variabile username
            postiPresi = postiLiberi[0:numBigliettiSelezionato]     #i posti che verranno occupati dalla prenotazione
            dataPagamento = getCurrentDateStr()                     #data del pagamento
            prezzoTotale = int(numBigliettiSelezionato) * Decimal(cardSelezionata.prezzoBase)
            email = request.form['user-email']                      #eventuale email immessa dall'utente

            serviziSelezionati = ServiziSelezionati(0, 0, 0, 0, 0, 0)   #in questo flusso di esecuzione non è stato selezionato alcun servizio aggiuntivo

            isOk = sendPayment(username, cardSelezionata, postiPresi, dataPagamento, str(prezzoTotale), '0', '0', str(prezzoTotale), serviziSelezionati, email)
            #se il pagamento è andato a buon fine, mostra all'utente la ricevuta di pagamento; altrimenti mostra un messaggio di errore
            if isOk:
                return render_template("PagamentoConcluso.html", username=username, card=cardSelezionata, numTickets=numBigliettiSelezionato, paymentDate=dataPagamento, basePrice=prezzoTotale, selectedSeats=postiPresi, seatsPrice='0', selectedServices=serviziSelezionati, servicesPrice='0', totalPrice=prezzoTotale, email=email)
            else:
                stringa = "SI È VERIFICATO UN ERRORE NELLA FINALIZZAZIONE DEL PAGAMENTO\nRIPROVARE PIÙ TARDI."
                return render_template("errore.html", errore=stringa, airline=None, username=username)

        else:
            stringa = "NON CI SONO POSTI LIBERI SUFFICIENTI\nPER IL NUMERO DI BIGLIETTI SELEZIONATO."
            return render_template("errore.html", errore=stringa, airline=None, username=username)
        
    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)
            


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
    if(not isinstance(diz, dict) or len(diz.keys())!= 12):
        session.pop(username)
        return redirect("/accedi",401)

    if request.method == 'POST':

        diz = session.get(username)
        session.pop(username)
        cardSelezionata = diz["cardSelezionata"]
        numBigliettiAcquistati = diz["numBigliettiAcquistati"]
        serviziSelezionati = diz["serviziSelezionati"]

        #tra le informazioni che ci servono abbiamo già lo username dell'utente racchiuso nella variabile username
        postiSelezionati = diz["postiSelezionati"]                      #i posti che verranno occupati dalla prenotazione
        dataPagamento = getCurrentDateStr()                             #data del pagamento
        prezzoBase = int(numBigliettiAcquistati) * Decimal(cardSelezionata.prezzoBase)  #prezzo base (moltiplicato per il numero di biglietti acquistati)
        prezzoSelezionePosti = diz["prezzoSelezionePosti"]              #prezzo dei posti a sedere selezionati
        prezzoServiziAggiuntivi = diz["prezzoServiziAggiuntivi"]        #prezzo dei servizi aggiuntivi selezionati
        prezzoTotale = diz["prezzoTotale"]                              #prezzo totale (base + selezione posti + servizi aggiuntivi)
        email = request.form['user-email']                              #eventuale email immessa dall'utente

        session[username] = diz

        isOk = sendPayment(username, cardSelezionata, postiSelezionati, dataPagamento, str(prezzoBase), str(prezzoSelezionePosti), str(prezzoServiziAggiuntivi), str(prezzoTotale), serviziSelezionati, email)
        #se il pagamento è andato a buon fine, mostra all'utente la ricevuta di pagamento; altrimenti mostra un messaggio di errore
        if isOk:
            return render_template("PagamentoConcluso.html", username=username, card=cardSelezionata, numTickets=numBigliettiAcquistati, paymentDate=dataPagamento, basePrice=prezzoBase, selectedSeats=postiSelezionati, seatsPrice=prezzoSelezionePosti, selectedServices=serviziSelezionati, servicesPrice=prezzoServiziAggiuntivi, totalPrice=prezzoTotale, email=email)
        else:
            stringa = "SI È VERIFICATO UN ERRORE NELLA FINALIZZAZIONE DEL PAGAMENTO.\nRIPROVARE PIÙ TARDI."
            return render_template("errore.html", errore=stringa, airline=None, username=username)

    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)


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
        diz['numBigliettiSelezionato'] = int(numBigliettiSelezionato)
        session[username] = diz
        prezzo_totale = int(numBigliettiSelezionato) * Decimal(cardSelezionata.prezzoBase)

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

    if(not isinstance(diz, dict) or len(diz.keys())!=6 or diz['username']!=username or diz['idVolo']!=idVolo):
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

        diz = session.get(username)
        session.pop(username)

        diz['postiSelezionati'] = postiSelezionati
        #I servizi aggiuntivi selezionati verranno inseriti all'interno della sessione ma raggruppati nell'oggetto Python per motivi di compattezza
        diz['serviziSelezionati'] = ServiziSelezionati(int(bagaglioSpeciale), int(bagaglioStivaMedio), int(bagaglioStivaGrande), int(assicurazioneBagagli), int(animaleDomestico), int(neonato))

        cardSelezionata = diz['cardSelezionata']
        prezziFilePosti = diz['prezziFilePosti']
        prezziServizi = diz['prezziServizi']

        #questa funzione restituisce una lista indicante il numero di posti selezionati per ogni gruppo di posti
        fileSelezionate = getFileSelezionate(postiSelezionati)        

        prezzoSelezionePosti = Decimal(prezziFilePosti.primo)*fileSelezionate[0] + Decimal(prezziFilePosti.secondo)*fileSelezionate[1] + Decimal(prezziFilePosti.terzo)*fileSelezionate[2] + Decimal(prezziFilePosti.quarto)*fileSelezionate[3] + Decimal(prezziFilePosti.quinto)*fileSelezionate[4]
        prezzoServiziAggiuntivi = Decimal(prezziServizi.bagaglioSpeciale)*int(bagaglioSpeciale) + Decimal(prezziServizi.bagaglioStivaMedio)*int(bagaglioStivaMedio) + Decimal(prezziServizi.bagaglioStivaGrande)*int(bagaglioStivaGrande) + Decimal(prezziServizi.assicurazioneBagagli)*int(assicurazioneBagagli) + Decimal(prezziServizi.animaleDomestico)*int(animaleDomestico) + Decimal(prezziServizi.neonato)*int(neonato)
        prezzoTotale = Decimal(cardSelezionata.prezzoBase)*len(postiSelezionati) + prezzoSelezionePosti + prezzoServiziAggiuntivi

        diz['numBigliettiAcquistati'] = len(postiSelezionati)
        diz['prezzoSelezionePosti'] = str(prezzoSelezionePosti)
        diz['prezzoServiziAggiuntivi'] = str(prezzoServiziAggiuntivi)
        diz['prezzoTotale'] = str(prezzoTotale)

        session[username] = diz

        if len(postiSelezionati) < 1 or len(postiSelezionati) > 20:
            stringa = "È NECESSARIO SELEZIONARE UN NUMERO DI POSTI NON INFERIORE A 1 E NON SUPERIORE A 20."
            return render_template("errore.html", errore=stringa, airline=None, username=username)

        return render_template("personalizzato.html", prezzoTotale = prezzoTotale, username = username, card = diz['cardSelezionata'])

    #Per gestire eventuali richieste di GET in cui vado a scrivere l'URL direttamente
    return redirect("/accedi", 302)


@app.route("/<string:username>/<string:compagnia>/<string:idVolo>/suggerimento")
def visualizzaSuggerimento(username, compagnia, idVolo):
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
    if(not isinstance(diz, dict) or (len(diz.keys())!=2) or diz['username']!=username):
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

    if(not check):
        """
        Nella URL è stato inserito l'identificativo di un volo insesistente,
        magari per sbaglio da parte dell'utente oppure come tentativo di attacco.
        Faccio la pop per eliminare lo stato della sessione poiché vengo
        reindirizzato all'accesso in cui non ho alcuno stato della sessione.
        """
        session.pop(username)
        return redirect("/accedi", 401)
   
    session.pop(username)
    session[username] = diz

    today = getCurrentDateStr()

    #chiamata gRPC per sapere quanti giorni prima del volo convenga acquistare i biglietti
    numDaysBefore = getNumDaysBefore(cardSelezionata, today)

    if numDaysBefore > 0:   #caso OK
        #conversione tra numero di giorni prima del volo e data 'assoluta' (che comunque deve essere una stringa)
        convenientDate = getConvenientDate(cardSelezionata.data, numDaysBefore)
        return render_template("Suggerimento.html", username=username, card=cardSelezionata, convenientDate=convenientDate)

    elif numDaysBefore == -1:   #caso in cui non c'era il training set nel microservizio Suggestions; in tal caso verrà indicata all'utente la data odierna
        convenientDate = getCurrentDateStr()
        return render_template("Suggerimento.html", username=username, card=cardSelezionata, convenientDate=convenientDate)

    else:       #caso in cui si è sollevata un'eccezione inaspettata
        stringa = "SI È VERIFICATO UN ERRORE INTERNO DEL SISTEMA.\nRIPROVARE PIÙ TARDI."
        return render_template("errore.html", errore=stringa, airline=None, username=username)


#logout
@app.route("/<string:username>/logout")
def logoutUtentePrenotazione(username):
    if session.get(username) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE."
        return render_template("errore.html", errore=stringa, airline=None, username=None)

    #termino la sessione relativa all'utente loggato
    session.pop(username)

    return redirect("/accedi")


@app.route("/<string:airline>/<string:username>/logout")
def logoutUtenteAirline(airline, username):
    if session.get(airline+username) is None:
        stringa = "ERRORE NELLA GESTIONE DELLA SESSIONE."
        return render_template("errore.html", errore=stringa, airline=None, username=None)

    #termino la sessione relativa all'utente loggato
    session.pop(airline+username)

    return redirect("/accedi")


#here the airline adds a new flight
@app.route("/<string:airline>/<string:username>/addFlight", methods=('GET', 'POST'))
def addFlight(airline, username):
    if session.get(airline + username) is None:
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

        response = sendNewFlight(flightId, date, departureAirport, arrivalAirport, fullDepartureHour, fullArrivalHour, airline, price, NUM_SEATS)

        #if new flight info is ok, then notify the user; else go back to addFlight page because the user has to change something
        if response.isOk:
            return redirect("/"+airline+"/"+username+"/Volo aggiunto")
        else:
            return render_template("errore.html", errore=response.error, airline=airline, username=username)

    return render_template("AddFlight.html", airline=airline, username=username)


#here the airline modifies the price of an existing flight
@app.route("/<string:airline>/<string:username>/modifyFlight", methods=('GET', 'POST'))
def modifyFlight(airline, username):
    if session.get(airline + username) is None:
        return redirect("/accedi", 302)

    if request.method == 'POST':

        flightId = request.form['inputId']
        newPrice = request.form['inputPrice']

        response = sendNewPrice(flightId, newPrice)

        if response.isOk:
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("errore.html", errore=response.error, airline=airline, username=username)

    return render_template("ModifyFlight.html", airline=airline, username=username)


#here the airline modifies the price for seat selection
@app.route("/<string:airline>/<string:username>/modifySeatsPrices", methods=('GET', 'POST'))
def modifySeatsPrices(airline, username):
    if session.get(airline + username) is None:
        return redirect("/accedi", 302)

    if request.method == 'POST':

        price1 = request.form['inputPrice1']
        price2 = request.form['inputPrice2']
        price6 = request.form['inputPrice6']
        price16 = request.form['inputPrice16']
        price18 = request.form['inputPrice18']

        response = sendSeatsPrices(airline, price1, price2, price6, price16, price18)

        if response.isOk:
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("errore.html", errore=response.error, airline=airline, username=username)

    return render_template("ModifySeatsPrices.html", airline=airline, username=username)


#here the airline modifies the price of extra-services
@app.route("/<string:airline>/<string:username>/modifyServicesPrices", methods=('GET', 'POST'))
def modifyServicesPrices(airline, username):
    if session.get(airline + username) is None:
        return redirect("/accedi", 302)

    if request.method == 'POST':

        priceBM = request.form['inputPrice1']
        priceBG = request.form['inputPrice2']
        priceBS = request.form['inputPrice3']
        priceAD = request.form['inputPrice4']
        priceAB = request.form['inputPrice5']
        priceTN = request.form['inputPrice6']

        response = sendServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN)

        if response.isOk:
            return redirect("/"+airline+"/"+username+"/Prezzi modificati")
        else:
            return render_template("errore.html", errore=response.error, airline=airline, username=username)

    return render_template("ModifyServicesPrices.html", airline=airline, username=username)


#here an ok message is shown
@app.route("/<string:airline>/<string:username>/<string:okMessage>", methods=('GET', 'POST'))
def showOkMessage(airline, username, okMessage):
    if session.get(airline + username) is None:
        return redirect("/accedi", 302)

    if request.method == 'POST':
        return redirect("/"+airline+"/"+username+"/airlineHome")

    return render_template("ManagementOk.html", airline=airline, username=username, okMessage=okMessage)


if __name__ == "__main__":
    app.run()
