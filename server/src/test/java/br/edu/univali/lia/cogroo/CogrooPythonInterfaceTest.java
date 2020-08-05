package br.edu.univali.lia.cogroo;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.IOException;

import org.cogroo.checker.CheckDocument;
import org.cogroo.entities.Mistake;
import org.cogroo.text.Document;
import org.cogroo.text.Sentence;
import org.cogroo.text.Token;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

public class CogrooPythonInterfaceTest {
    static CogrooPythonInterface app;

    @BeforeAll
    static void setup() throws IOException {
        app = new CogrooPythonInterface();
    }

    @Test
    void testSimpleSentenceWithGrammarMistake() {
        Document document = app.analyze("Minhas flores é laranjas.");
        assertEquals(document.getSentences().size(), 1);

        Sentence sentence = document.getSentences().get(0);
        assertEquals(sentence.getTokens().size(), 5);
        assertEquals(sentence.getText(), "Minhas flores é laranjas.");

        Token secondToken = document.getSentences().get(0).getTokens().get(1);
        assertEquals(secondToken.getLemmas()[0], "flor");
        assertEquals(secondToken.getLexeme(), "flores");
        assertEquals(secondToken.getPOSTag(), "n");
        assertEquals(secondToken.getStart(), 7);

        CheckDocument gcDocument = (CheckDocument) app.grammarCheck("Minhas flores é laranjas.");
        assertEquals(gcDocument.getSentences().size(), 1);

        Sentence gcSentence = gcDocument.getSentences().get(0);
        assertEquals(gcSentence.toString(), sentence.toString());

        assertEquals(gcDocument.getMistakes().size(), 1);
        Mistake mistake = gcDocument.getMistakes().get(0);
        assertEquals(mistake.getRuleIdentifier(), "xml:127");
        assertEquals(mistake.getShortMessage(), "O adjetivo na função de predicativo concorda com o sujeito.");

        gcDocument = (CheckDocument) app.grammarCheck("Elas são bonita.");
        assertEquals(gcDocument.getMistakes().size(), 1);
    }
}