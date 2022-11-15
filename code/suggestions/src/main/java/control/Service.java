package control;

import java.io.*;
import java.lang.Math;

import io.grpc.stub.StreamObserver;

import control.proto.SuggestionsServiceGrpc.SuggestionsServiceImplBase;
import control.proto.SelectedFlight;
import control.proto.SelectionResponse;

import utils.LogUtil;

public class Service extends SuggestionsServiceImplBase {

    @Override
    public void getLogFileBoo(GetLogFileRequestSug req, StreamObserver<GetLogFileReplySug> responseObserver) {

        LogUtil opfile = new LogUtil();
        opfile.createLog();                 //creazione del file di log
        opfile.writeLog("[LOGGING] richiesta dati di logging...\n\n");

        final int chunkDim = 1000;      //in Python era una macro
        int r = -1;
        int q = -1;

        try(FileReader rd = new FileReader("suggestions.log")) {

            BufferedReader bReader = new BufferedReader(rd);
            String content = "";         //the whole content of suggestions.log
            String line;
            int count, lowerBound;

            while(true) {
                line = bReader.readLine();
                if(line==null)      //se line==null vuol dire che il file è finito e non è stata trovata alcuna riga col valore true
                    break;

                content+=line;

            }
            bReader.close();

        }

        int dim = content.length();
        q = Math.floor(dim/chunkDim);
        r = dim % chunkDim;

        if(q==0) {
            //TODO: farsi spiegare da Luca come diavolo funziona lo yield nell'ambito gRPC

        }
        else {
            count = 0;

            for(int i=0; i<q; i++) {
                try {
                    //TODO
                }
                catch(Exception e) {
                    opfile.writeLog("[LOGGING] Dati di logging inviati senza successo.");
                }
                count++;

            }
            if(r>0) {
                lowerBound = count*chunkDim;
                //TODO

            }

        }
        opfile.writeLog("[LOGGING] Dati di logging inviati con successo.");

        try(RandomAccessFile raf = new RandomAccessFile("suggesions.log", "rw")) {
            raf.setLength(0);   //to erase all data
        }

    }


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
