package model;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class PastFlight {

    private Date bookingDate;
    private Date flightDate;
    private String departureAirport;
    private String arrivalAirport;
    private String airline;
    private double price;

    private long remainingDays;
    private String isConvenient;

    public PastFlight(Date bookingDate, Date flightDate, String departureAirport, String arrivalAirport, String airline, double price) {
        
        this.bookingDate = bookingDate;
        this.flightDate = flightDate;
        this.departureAirport = departureAirport;
        this.arrivalAirport = arrivalAirport;
        this.airline = airline;
        this.price = price;

        this.remainingDays = (flightDate.getTime() - bookingDate.getTime()) / 86400000L;
        this.isConvenient = "false";

    }

    public Date getBookingDate() {
        return this.bookingDate;
    }

    public void setBookingDate(Date bookingDate) {
        this.bookingDate = bookingDate;
        this.remainingDays = (this.flightDate.getTime() - bookingDate.getTime()) / 86400000L;
    }

    public Date getFlightDate() {
        return this.flightDate;
    }

    public void setFlightDate(Date flightDate) {
        this.flightDate = flightDate;
        this.remainingDays = (flightDate.getTime() - this.bookingDate.getTime()) / 86400000L;
    }

    public String getDepartureAirport() {
        return this.departureAirport;
    }

    public void setDepartureAirport(String departureAirport) {
        this.departureAirport = departureAirport;
    }

    public String getArrivalAirport() {
        return this.arrivalAirport;
    }

    public void setArrivalAirport(String arrivalAirport) {
        this.arrivalAirport = arrivalAirport;
    }

    public String getAirline() {
        return this.airline;
    }

    public void setAirline(String airline) {
        this.airline = airline;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public long getRemainingDays() {
        return this.remainingDays;
    }

    public String isConvenient() {
        return this.isConvenient;
    }

    public void setConvenient(String isConvenient) {
        if(isConvenient.equals("true") || isConvenient.equals("false")) {
            this.isConvenient = isConvenient;
        }
    }

}
