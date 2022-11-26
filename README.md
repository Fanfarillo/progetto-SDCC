# Progetto SDCC - tipologia A2
Per poter utilizzare l'applicazione, pensata per essere eseguita in un sistema Unix (in particolare noi abbiamo utilizzato Ubuntu), è necessario aver installato nel proprio PC:
- Git
- Python 3
- La libreria boto3 di Python
- AWS CLI
- Docker
- Docker Compose

##Installazione dell'applicazione
Per installare l'applicazione all'interno del proprio PC, è sufficiente eseguire il seguente comando: git clone https://github.com/Fanfarillo/progetto-SDCC.git.

## Configurazione dell'applicazione
È possibile istanziare e pre-popolare le tabelle (chiave, valore) relative ai microservizi stateless su DynamoDB lanciando lo script CreateTables.sh (che si trova all'interno della directory /code/initialization). È altresì possibile eliminare tali tabelle mediante lo script RemoveTables.sh (che si trova all'interno della directory /code).<br>
Tuttavia, per essere in grado di eseguire queste operazioni, è necessario avere un Learner Lab di AWS attivo e il token relativo a tale Learner Lab correttamente configurato all'interno del file ~/.aws/credentials.<br>

## Avvio dell'applicazione
Prima di avviare l'applicazione, è nuovamente necessario avere un Learner Lab di AWS attivo. Stavolta, il token associato al Lab deve essere copiato all'interno di un file che deve essere rinominato "credentials"; tale file deve essere inserito in tutte le seguenti directory: /code/booking, /code/discovery, /code/frontend, /code/logging, /code/management, /code/payment, /code/registration, /code/suggestions.<br>
A questo putno, per far partire l'applicazione, basta eseguire lo script Startup.sh (che si trova all'interno della directory /code).

## Spegnimento dell'applicazione
Per interrompere l'esecuzione dell'applicazione, è sufficiente eseguire lo script Shutdown.sh (che si trova all'interno della directory /code).<br>
Se si vogliono eliminare i container Docker che vengono istanziati per far funzionare l'applicazione, si utilizza lo script RemoveContainers.sh (che si trova all'interno della directory /code).<br>
Se si vogliono eliminare anche le immagini Docker relative ai container, si ricorre allo script RemoveAll.sh (che si trova all'interno della directory /code).
