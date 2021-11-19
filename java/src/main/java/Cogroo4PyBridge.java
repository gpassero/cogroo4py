import java.io.IOException;
import java.util.Locale;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.cogroo.analyzer.Analyzer;
import org.cogroo.analyzer.ComponentFactory;
import org.cogroo.checker.CheckDocument;
import org.cogroo.checker.GrammarChecker;
import org.cogroo.text.Document;
import org.cogroo.text.impl.DocumentImpl;

public class Cogroo4PyBridge {

    public ComponentFactory factory = ComponentFactory.create(new Locale("pt", "BR"));
    public Analyzer cogroo;
    public GrammarChecker gc;

    public static void main(String[] args) throws IllegalArgumentException, IOException {
        Cogroo4PyBridge app = new Cogroo4PyBridge();
    }

    public Cogroo4PyBridge() throws IllegalArgumentException, IOException {
        cogroo = factory.createPipe();
        gc = new GrammarChecker(cogroo);
        Logger globalLogger = Logger.getLogger(java.util.logging.Logger.GLOBAL_LOGGER_NAME);
        globalLogger.setLevel(Level.DEBUG);
        Logger cogrooLogger = Logger.getLogger("org.cogroo.interpreters.FlorestaTagInterpreter");
        cogrooLogger.setLevel(Level.DEBUG);
        Logger.getRootLogger().setLevel(Level.DEBUG);
    }

    public Document analyze(String text) {
        System.out.println("Text received for analysis: " + text);
        DocumentImpl doc = new DocumentImpl();
        doc.setText(text);
        cogroo.analyze(doc);
        return doc;
    }

    public Document grammarCheck(String text) {
        System.out.println("Text received for analysis: " + text);
        CheckDocument doc = new CheckDocument(text);
        gc.analyze(doc);
        return doc;
    }

}