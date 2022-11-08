package utils;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LogUtil {

    private FileHandler fh;

    public void createLog() {
        try {
            this.fh = new FileHandler("suggestions.log", true);

        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }

    public void writeLog(String message) {
        try {
            Logger logger = Logger.getLogger("BookLog");
            logger.addHandler(this.fh);
            logger.setLevel(Level.ALL);
            SimpleFormatter formatter = new SimpleFormatter();
            this.fh.setFormatter(formatter);
            logger.log(Level.ALL, message);

        }
        catch(Exception e) {
            e.printStackTrace();
        }

    }

}