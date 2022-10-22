package utils;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class DateUtil {

    public static Date getDateObject(String dateStr) throws ParseException {

        DateFormat df = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
        df.setLenient(false);   //in tal modo, le stringhe relative alle date devono matchare perfettamente col pattern "dd-MM-yyyy"
        return df.parse(dateStr);

    }

}
