package control;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOExcpetion;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.nio.file.Files;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import weka.classifiers.trees.RandomForest;
import weka.core.Instances;

import utils.PastFlightUtil;
import utils.DateUtil;

public class PopulateArff {

    public static void storeNewData(String message) throws ParseException, IOExcpetion {

        /* Il messaggio (associato a uno specifico volo V) è composto da tante righe ciascuna delle quali è relativo a uno specifico giorno in cui si poteva
         * prenotare V. Ciaascuna riga è fatta così:
         * Data_prenotazione,data_volo,aeroporto_partenza,aeroporto_arrivo,compagnia_aerea,prezzo_base */
        List<PastFlight> pastFlights = PastFlightUtil.instantiatePastFligths(message);
        
        try(FileWriter wr = new FileWriter("Train.arff", true)) {   //true == sto aprendo il FileWriter in append; in tal modo non sovrascrivo i dati esistenti
            for(PastFlight pastFlight : pastFlights) {
                
                wr.write(pastFlight.remainingDays.toString() + "," + pastFlight.airline + "," + pastFlight.departureAirport + "," + pastFlight.arrivalAirport +
                    "," + pastFlight.isConvenient + "\n");

            }

        }

    }

    public static void createTestingSet(String bookingDateStr, String flightDateStr, String airline, String departureAirport, String arrivalAirport) throws ParseException, IOExcpetion {

        Date bookingDate = DateUtil.getDateObject(bookingDateStr);
        Date flightDate = DateUtil.getDateObject(flightDateStr);
        long remainingDays = (flightDate.getTime() - bookingDate.getTime()) / 86400000L;

        try(FileWriter wr = new FileWriter("Test.arff")) {

            //inseriremo un'istanza nel testing set per ogni giorno rimanente al volo
            for(long i=remainingDays; i>0; i--) {       //stiamo andando dalla data più vicina a oggi alla data più lontana da oggi
                wr.write(i.toString()+ "," + airline + "," + departureAirport + "," + arrivalAirport + ",?\n");
            }

        }

        storeLabeledTestingSet();   //generazione del testing set etichettato ("labeled")

        /* TODO: scandire il file Labeled.arff per ottenere la prima riga contenente ",true". 
         * Di tale riga bisognerà recuperare il primo valore (che è il numero relativo ai giorni rimanenti al volo).
         * Se non ci sarà alcun true, allora prendere remainingDays.
         * Il valore considerato dovrà essere ritornato al chiamante. */

    }

    public static void storeLabeledTestingSet() {

        BufferedReader bReader = null;
        bReader = new BufferedReader(new FileReader("Train.arff"));
        Instances train = new Instances(bReader);
        train.setClassIndex(train.numAttributes()-1);

        bReader = new BufferedReader(new FileReader("Test.arff"));
        Instances test = new Instances(bReader);
        test.setClassIndex(train.numAttributes()-1);

        bReader.close();

        RandomForest tree = new RandomForest();     //new instance of tree
        tree.buildClassifier(train);                //build classifier
        Instances labeled = new Instances(test);

        //label instances in testing set
        for(int i=0; i<test.numInstances(); i++) {
            double clsLabel = tree.classifyInstance(test.instance(i));
            labeled.instance(i).setClassValue(clsLabel);
        }
        
        //save labeled data in a new file
        BufferedWriter bWriter = new BufferedWriter(new FileWriter("Labeled.arff"));
        bWriter.write(labeled.toString());

        bWriter.close();

    }

}
