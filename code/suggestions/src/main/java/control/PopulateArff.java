package control;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.nio.file.Files;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.ArrayList;
import java.util.List;

import weka.classifiers.trees.RandomForest;
import weka.core.Instances;
import weka.core.WekaException;

import model.PastFlight;
import utils.PastFlightUtil;
import utils.DateUtil;

public class PopulateArff {

    public static boolean storeNewData(String message) {

        try {            
            /* Il messaggio (associato a uno specifico volo V) è composto da tante righe ciascuna delle quali è relativa a uno specifico giorno in cui si poteva
             * prenotare V. Ciascuna riga è fatta così:
             * Data_prenotazione,data_volo,aeroporto_partenza,aeroporto_arrivo,compagnia_aerea,prezzo_base */
            List<PastFlight> pastFlights = PastFlightUtil.instantiatePastFlights(message);
        
            try(FileWriter wr = new FileWriter("Train.arff", true)) {   //true == sto aprendo il FileWriter in append; in tal modo non sovrascrivo i dati esistenti
               for(PastFlight pastFlight : pastFlights) {
                
                    wr.write(Long.toString(pastFlight.getRemainingDays()) + "," + pastFlight.getAirline() + "," + pastFlight.isConvenient() + "\n");

                }
                return true;

            }

        }
        catch(Exception e) {
            e.printStackTrace();
            return false;
        }

    }

    public static void storeLabeledTestingSet() throws Exception {

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

    public static int getNumDaysBeforeConv(long remainingDays) throws Exception {

        BufferedReader bReader = new BufferedReader(new FileReader("Labeled.arff"));
        String line;
        int numDaysBeforeConv = (int) remainingDays;    //valore di default per il numero di giorni in anticipo in cui conviene prenotare il volo

        while(true) {
            line = bReader.readLine();
            if(line==null)      //se line==null vuol dire che il file è finito e non è stata trovata alcuna riga col valore true;
                break;          //in tal caso si ricorre al valore di default per il numero di giorni in anticipo in cui conviene prenotare il volo

            if(line.contains(",true")) {
                //se esiste una riga col valore true, numDaysBeforeConv assume il valore del primo attributo proprio di quella riga
                String[] attributes = line.split(",");
                numDaysBeforeConv = Integer.parseInt(attributes[0]);
                break;

            }

        }

        return numDaysBeforeConv;

    }

    public static int createTestingSet(String bookingDateStr, String flightDateStr, String airline) {

        try {
            Date bookingDate = DateUtil.getDateObject(bookingDateStr);
            Date flightDate = DateUtil.getDateObject(flightDateStr);
            long remainingDays = (flightDate.getTime() - bookingDate.getTime()) / 86400000L;

            try(FileWriter wr = new FileWriter("Test.arff")) {

                wr.write("@relation Test\n");
                wr.write("@attribute REM_DAYS numeric\n");
                wr.write("@attribute AIRLINE {'Ryanair', 'EasyJet', 'ITA'}\n");
                wr.write("@attribute IS_CONVENIENT {'true', 'false'}\n");
                wr.write("@data\n");

                //inseriremo un'istanza nel testing set per ogni giorno rimanente al volo
                for(long i=remainingDays; i>0; i--) {       //stiamo andando dalla data più vicina a oggi alla data più lontana da oggi
                    wr.write(Long.toString(i)+ "," + airline + ",?\n");
                }

            }

            storeLabeledTestingSet();   //generazione del testing set etichettato ("labeled")

            /* A questo punto bisogna scandire il file Labeled.arff per ottenere la prima riga contenente ",true". 
            * Di tale riga bisognerà recuperare il primo valore (che è il numero relativo ai giorni rimanenti al volo).
            * Se non ci sarà alcun true, allora prendere remainingDays.
            * Il valore considerato dovrà essere ritornato al chiamante. */
            return getNumDaysBeforeConv(remainingDays);

        }
        catch(WekaException e1) {
            return -1;  //se viene sollevata una WekaException, significa che il training set è vuoto; in tal caso, verrà detto al client che conviene prenotare oggi
                        //NB: il valore di ritorno -1 verrà convertito correttamente nella data odierna dal frontend.
        }
        catch(Exception e2) {
            e2.printStackTrace();
            return -2;  //se viene sollevata un'eccezione diversa, restituisci -2 al client, in modo tale da notificargli una condizione di errore
        }

    }

}
