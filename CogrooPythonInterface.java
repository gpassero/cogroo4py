import java.io.IOException;
import java.util.Locale;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.cogroo.analyzer.Analyzer;
import org.cogroo.analyzer.ComponentFactory;
import org.cogroo.text.Document;
import org.cogroo.text.impl.DocumentImpl;

import py4j.GatewayServer;

public class CogrooPythonInterface {
	
	public ComponentFactory factory = ComponentFactory.create(new Locale("pt", "BR"));
	public Analyzer cogroo;
	
	public static void main(String[] args) throws IllegalArgumentException, IOException {		
		CogrooPythonInterface app = new CogrooPythonInterface();
	    GatewayServer server = new GatewayServer(app);
	    server.start();	
	    System.out.println("Gateway Server Started");	   	   
	}
	
	public CogrooPythonInterface() throws IllegalArgumentException, IOException {
		cogroo = factory.createPipe();		
		Logger globalLogger = Logger.getLogger(java.util.logging.Logger.GLOBAL_LOGGER_NAME);
		globalLogger.setLevel(Level.OFF);
		Logger cogrooLogger = Logger.getLogger("org.cogroo.interpreters.FlorestaTagInterpreter");
		cogrooLogger.setLevel(Level.OFF);	
		Logger.getRootLogger().setLevel(Level.OFF); 
	}
	
	public Document analyze(String text) {
		System.out.println("Text received for analysis: " + text);
		DocumentImpl doc = new DocumentImpl();
		doc.setText(text);		
		cogroo.analyze(doc);
		return doc;
	}
	
}
