package control;

import io.grpc.stub.StreamObserver;

import control.proto.SuggestionsServiceGrpc.SuggestionsServiceImplBase;
import control.proto.SelectedFlight;
import control.proto.SelectionResponse;

import utils.LogUtil;

public class Service extends SuggestionsServiceImplBase {

    @Override   //getSelectedFlight or getNumDaysBeforeConvenient?
    public void getSelectedFlight(SelectedFlight req, StreamObserver<SelectionResponse> responseObserver) {

        //questa funzione genera il testing set in base al volo selezionato dall'utente e al numero di giorni rimanenti al volo;
        //in particolare, vengono prese in considerazione le istanze relative a una compagnia aerea, un aeroporto di partenza e un aeroporto di arrivo;
        //tali istanze avranno come 'numero di giorni rimanenti al volo' un valore compreso tra 1 e il numero ATTUALE di giorni rimanenti al volo
        LogUtil opfile = new LogUtil();
        opfile.createLog();                 //creazione del file di log
        opfile.writeLog("Richiesta di suggerimenti riguardanti un volo.");

        //i metodi get() applicati a req sono propri di gRPC; non c'entrano nulla con i getter di PastFlight
        int output = PopulateArff.createTestingSet(req.getBookingDate(), req.getFlightDate(), req.getAirline(), req.getDepartureAirport(), req.getArrivalAirport());

        //output è il numero di giorni prima del volo in cui conviene effettuare l'acquisto dei biglietti
        SelectionResponse response = SelectionResponse.newBuilder().setNumDaysBeforeConvenient(output).build();

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

    @Override
    public void storeOldFlight(OldFlight req, StreamObserver<StoreOldResponse> responseObserver) {

        //questa funzione riceve nuovi dati da aggiungere poi al training set
        LogUtil opfile = new LogUtil();
        opfile.createLog();                 //creazione del file di log
        opfile.writeLog("Richiesta di aggiunta di nuovi dati al training set.");

        boolean output = PopulateArff.storeNewData(req.getOldFlightsMsg());

        //output è il numero di giorni prima del volo in cui conviene effettuare l'acquisto dei biglietti
        StoreOldResponse response = StoreOldResponse.newBuilder().setIsOk(output).build();

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

}
