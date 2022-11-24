package utils;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LogUtil {

    private static LogUtil instance = null;     //logUtil è una classe SINGLETON
    private FileHandler fh = null;

    //il costruttore delle classi singleton non può essere pubblico
    protected LogUtil() {
        try {
            this.fh = new FileHandler("suggestions.log", true);

        }
        catch(Exception e) {
            e.printStackTrace();
        }

    }

    //getInstance è il metodo pubblico per l'istanziazione delle classi singleton
    public static synchronized LogUtil getInstance() {
        if(LogUtil.instance==null)
            LogUtil.instance = new LogUtil();
        
        return LogUtil.instance;

    }

    public synchronized void writeLog(String message) {
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
