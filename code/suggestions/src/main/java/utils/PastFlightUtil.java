package utils;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.ArrayList;
import java.util.List;

import model.PastFlight;

public class PastFlightUtil {

    public static List<PastFlight> instantiatePastFligths(String message) throws ParseException {

        //singleDaysMsg è un array che contiene tante stringhe quanti erano i giorni in cui era potenzialmente possibile prenotare il volo
        String[] singleDaysMsg = message.split("\n");
        
        //pastFlights è una lista che conterrà tanti oggetti di tipo PastFlight che mantengono le informazioni di un particolare volo,
        //incluso il prezzo del biglietto in uno specifico giorno antecedente al volo
        List<PastFlight> pastFlights = new ArrayList<>();

        double pricesSum = 0.0;     //somma di tutti i prezzi dello stesso volo al variare dei giorni; tale variabile servirà per calcolare il prezzo medio del volo

        for(int i=0; i<singleDaysMsg.length; i++) {

            /* singleDayInfo è un array di stringhe che contiene nell'ordine: 
             * Data prenotazione
             * Data volo
             * Aeroporto partenza
             * Aeroporto arrivo
             * Compagnia aerea
             * Prezzo base */
            String[] singleDayInfo = singleDaysMsg[i].split(",");

            String departureAirport = singleDayInfo[2];
            String arrivalAirport = singleDayInfo[3];
            String airline = singleDayInfo[4];

            Date bookingDate = DateUtil.getDateObject(singleDayInfo[0]);
            Date flightDate = DateUtil.getDateObject(singleDayInfo[1]);

            double price = Double.parseDouble(singleDayInfo[5]);
            pricesSum = pricesSum+price;

            PastFlight flight = new PastFlight(bookingDate, flightDate, departureAirport, arrivalAirport, airline, price);
            pastFlights.add(flight);

        }

        double avgPrice = pricesSum/singleDaysMsg.length;
        
        for(PastFlight pastFlight : pastFlights) {
            //se in un determinato giorno il prezzo del biglietto era al di sotto la media, allora quel giorno era da considerarsi conveniente per l'acquisto
            if(pastFlight.getPrice() < avgPrice) {
                pastFlight.setConvenient("true");
            }

        }

        return pastFlights;

    }

}
