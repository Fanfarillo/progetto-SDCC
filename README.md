# Progetto SDCC - tipologia A2
Per poter utilizzare l'applicazione, pensata per essere eseguita in un sistema Unix (in particolare noi abbiamo utilizzato Ubuntu), è necessario aver installato nel proprio PC:
- Python 3
- La libreria boto3 di Python
- Docker
- Docker Compose

## Configurazione dell'applicazione
E' possibile istanziare e pre-popolare le tabelle (chiave, valore) relative ai microservizi stateless su DynamoDB lanciando lo script CreateTables.sh (che si trova all'interno della directory /code/initialization).
E' altresì possibile eliminare tali tabelle mediante lo script RemoveTables.sh (che si trova all'interno della directory /code).

## Avvio dell'applicazione
Per far partire l'applicazione, basta eseguire lo script Startup.sh (che si trova all'interno della directory /code).

## Spegnimento dell'applicazione
Per interrompere l'esecuzione dell'applicazione, è sufficiente eseguire lo script Shutdown.sh (che si trova all'interno della directory /code).
Se si vogliono eliminare anche le immagini Docker relative ai container che vengono istanziati per far funzionare l'applicazione, si ricorre allo script RemoveImages.sh (che si trova all'interno della directory /code).