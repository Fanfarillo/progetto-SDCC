package control;

import io.grpc.stub.StreamObserver;

import control.proto.SuggestionsServiceGrpc.SuggestionsServiceImplBase;
import control.proto.SelectedFlight;
import control.proto.SelectionResponse;

public class Service extends SuggestionsServiceImplBase {

    @Override
    public void getSelectedFlight(SelectedFlight req, StreamObserver<SelectionResponse> responseObserver) {    //getSelectedFlight or getNumDaysBeforeConvenient?

        //questa funzione genera il testing set in base al volo selezionato dall'utente e al numero di giorni rimanenti al volo;
        //in particolare, vengono prese in considerazione le istanze relative a una compagnia aerea, un aeroporto di partenza e un aeroporto di arrivo;
        //tali istanze avranno come 'numero di giorni rimanenti al volo' un valore compreso tra 1 e il numero ATTUALE di giorni rimanenti al volo
        PopulateArff.createTestingSet(req.getBookingDate, req.getFlightDate, req.getAirline, req.getDepartureAirport, req.getArrivalAirport);

        //response for the client
        SelectionResponse response = SelectionResponse.newBuilder().setNumDaysBeforeConvenient(1).build();      //TODO: change parameter 1

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

}
