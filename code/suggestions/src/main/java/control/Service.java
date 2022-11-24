package control;

import java.io.*;
import java.lang.Math;

import com.google.protobuf.ByteString;
import io.grpc.stub.StreamObserver;

import control.proto.SuggestionsServiceGrpc.SuggestionsServiceImplBase;
import control.proto.SelectedFlight;
import control.proto.SelectionResponse;
import control.proto.OldFlight;
import control.proto.StoreOldResponse;
import control.proto.GetLogFileRequestSug;
import control.proto.GetLogFileReplySug;  

import utils.LogUtil;

public class Service extends SuggestionsServiceImplBase {

    @Override
    public void getLogFileSug(GetLogFileRequestSug req, StreamObserver<GetLogFileReplySug> responseObserver) {

        LogUtil opfile = LogUtil.getInstance();     //ottenimento del file di log
        opfile.writeLog("[LOGGING] Richiesta dati di logging...\n\n");

        final int chunkDim = 1000;      //in Python era una macro
        int r = -1;
        int q = -1;

        String content = "";            //the whole content of suggestions.log
        int count, lowerBound;

        try(FileReader rd = new FileReader("suggestions.log")) {

            BufferedReader bReader = new BufferedReader(rd);
            String line;

            while(true) {
                line = bReader.readLine();
                if(line==null)      //se line==null vuol dire che il file è finito e non è stata trovata alcuna riga col valore true
                    break;

                content+=line;

            }
            bReader.close();

        }
        catch(Exception e) {
            opfile.writeLog("[LOGGING] Un'eccezione è stata sollevata durante l'esecuzione della funzione getLogFileSug.");
        }

        int dim = content.length();
        q = (int)Math.floor(dim/chunkDim);
        r = dim % chunkDim;

        if(q==0) {
            //EQUIVALENTE DI: yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto.encode(), num_chunk=0)
            GetLogFileReplySug response = GetLogFileReplySug.newBuilder().setChunkFile(ByteString.copyFromUtf8(content)).setNumChunk(0).build();
            responseObserver.onNext(response);

        }
        else {
            count = 0;

            for(int i=0; i<q; i++) {
                try {
                    //EQUIVALENTE DI: yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto[i:i+CHUNK_DIM].encode(), num_chunk=i)
                    GetLogFileReplySug response = GetLogFileReplySug.newBuilder().setChunkFile(ByteString.copyFromUtf8(content.substring(i*chunkDim,i*chunkDim+chunkDim))).setNumChunk(i).build();
                    responseObserver.onNext(response);
                }
                catch(Exception e) {
                    opfile.writeLog("[LOGGING] Dati di logging inviati senza successo.");
                }
                count++;

            }
            if(r>0) {
                lowerBound = count*chunkDim;
                //EQUIVALENTE DI: yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto[lower_bound:lower_bound+r].encode(), num_chunk=count)
                GetLogFileReplySug response = GetLogFileReplySug.newBuilder().setChunkFile(ByteString.copyFromUtf8(content.substring(lowerBound,lowerBound+r))).setNumChunk(count).build();
                responseObserver.onNext(response);

            }

        }
        opfile.writeLog("[LOGGING] Dati di logging inviati con successo.");

        try(RandomAccessFile raf = new RandomAccessFile("suggestions.log", "rw")) {
            raf.setLength(0);   //to erase all data
        }
        catch(Exception e) {
            opfile.writeLog("[LOGGING] Un'eccezione è stata sollevata durante l'esecuzione della funzione getLogFileSug.");
        }

        responseObserver.onCompleted();

    }


    @Override
    public void getSelectedFlight(SelectedFlight req, StreamObserver<SelectionResponse> responseObserver) {
        /*DISCLAIMER: il messaggio di richiesta req comprende anche gli aeroporti di partenza e di arrivo dei voli;
         *tuttavia, durante la fase di debugging ne è stato eliminato l'utilizzo perché i classificatori di Machine Learning
         *non sono in grado di trattare le stringhe come attributi delle istanze. */

        //questa funzione genera il testing set in base al volo selezionato dall'utente e al numero di giorni rimanenti al volo;
        //in particolare, vengono prese in considerazione le istanze relative a una compagnia aerea;
        //tali istanze avranno come 'numero di giorni rimanenti al volo' un valore compreso tra 1 e il numero ATTUALE di giorni rimanenti al volo
        LogUtil opfile = LogUtil.getInstance();     //ottenimento del file di log
        opfile.writeLog("Richiesta di suggerimenti riguardanti un volo.");

        //i metodi get() applicati a req sono propri di gRPC; non c'entrano nulla con i getter di PastFlight
        int output = PopulateArff.createTestingSet(req.getBookingDate(), req.getFlightDate(), req.getAirline());
        opfile.writeLog("Richiesta di suggerimenti riguardanti un volo completata.");

        //output è il numero di giorni prima del volo in cui conviene effettuare l'acquisto dei biglietti
        SelectionResponse response = SelectionResponse.newBuilder().setNumDaysBeforeConvenient(output).build();

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }
    

    @Override
    public void storeOldFlight(OldFlight req, StreamObserver<StoreOldResponse> responseObserver) {
        /*DISCLAIMER: il messaggio di richiesta req comprende anche gli aeroporti di partenza e di arrivo dei voli;
         *tuttavia, durante la fase di debugging ne è stato eliminato l'utilizzo perché i classificatori di Machine Learning
         *non sono in grado di trattare le stringhe come attributi delle istanze. */

        //questa funzione riceve nuovi dati da aggiungere poi al training set
        LogUtil opfile = LogUtil.getInstance();     //ottenimento del file di log
        opfile.writeLog("Richiesta di aggiunta di nuovi dati al training set.");

        boolean output = PopulateArff.storeNewData(req.getOldFlightsMsg());

        //output è il numero di giorni prima del volo in cui conviene effettuare l'acquisto dei biglietti
        StoreOldResponse response = StoreOldResponse.newBuilder().setIsOk(output).build();

        //se si è la copia primaria di Suggestions, bisogna invocare la copia secondaria per mantenerla allineata con gli aggiornamenti
        if(Suggestions.ownIpAddress.equals(Suggestions.suggestions1)) {
            SugClient.sendToSecondary(req.getOldFlightsMsg());
            opfile.writeLog("Nuovi dati per il training set inviati anche alla replica secondaria.");
        }

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

}
