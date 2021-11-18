# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 21:21:19 2016

@author: Guilherme Passero <guilherme.passero0@gmail.com>
"""
import cogroo4py.jpype_config  # noqa
import inspect
import os

from functools import lru_cache
import logging
import re
import subprocess

from retry import retry

from java.util import Locale
from org.cogroo.analyzer import ComponentFactory
from org.cogroo.checker import GrammarChecker, CheckDocument
from org.cogroo.text import Document as CogrooDocument
from org.cogroo.text import Sentence as CogrooSentence
from org.cogroo.text import Token as CogrooToken
from org.cogroo.text import Chunk as CogrooChunk
from org.cogroo.text.impl import DocumentImpl

LOGGER = logging.getLogger(__name__)


class CogrooAnalyzer:
    def __init__(self):
        self._cogroo = ComponentFactory.create(Locale('pt', 'BR')).createPipe()
        self._grammar_checker = GrammarChecker(self._cogroo)

    def analyze(self, text: str) -> CogrooDocument:
        document = DocumentImpl()
        document.setText(text)
        self._cogroo.analyze(document)
        return document

    def grammar_check(self, text: str) -> CogrooDocument:
        document = CheckDocument(text)
        self._grammar_checker.analyze(document)
        return document


def find(pattern, text):
    return [(i.start(), i.end()) for i in re.finditer(pattern, text)]


class Token:
    def __init__(self, cogroo_token: CogrooToken):
        self.lemmas = list(cogroo_token.getLemmas())
        self.lexeme = cogroo_token.getLexeme()

        if len(self.lemmas) > 0:
            self.lemma = self.lemmas[0]
        else:
            self.lemma = self.lexeme

        self.lemma = self.lemma.replace('_', ' ')
        self.chunk = cogroo_token.getChunkTag()
        self.chunk_head = cogroo_token.isChunkHead()
        self.synchunk = cogroo_token.getSyntacticTag()
        self.pos = cogroo_token.getPOSTag()
        self.feat = cogroo_token.getFeatures()
        self.start = cogroo_token.getStart()
        self.end = cogroo_token.getEnd()
# TODO analyze when number to string conversion may be useful
#        if self.pos == 'num' and re.match('\d+[.,]?\d*', self.lemma):
#            try:
#                num = float(self.lemma.replace(',', '.'))
#                self.lemma = num2words(num, lang='pt_BR')
#            except:
#                print('Couldn\'t convert ' + self.lemma + ' to number.')

    def __repr__(self):
        return '{0}#{1} {2}'.format(self.lexeme, self.pos, self.feat)


class Chunk:
    def __init__(self, sentence: "Sentence", cogroo_chunk: CogrooChunk):
        self.tag = cogroo_chunk.getTag()
        tokens = cogroo_chunk.getTokens()
        if len(tokens) > 0:
            self.start = tokens[0].getStart()
            self.end = tokens[-1].getEnd()
            self.tokens = []
            for token in sentence.tokens:
                if token.start >= self.start and token.end <= self.end:
                    self.tokens.append(token)

                elif token.end > self.end:
                    break

    def __repr__(self):
        return self.tag + '[' + repr(self.tokens) + ']'


class Sentence:
    def __init__(self, cogroo_sentence: CogrooSentence, paragraph: int):
        self.text = cogroo_sentence.getText()
        self.start = cogroo_sentence.getStart()
        self.end = cogroo_sentence.getEnd()
        self.paragraph = paragraph
        self.tokens = []
        for token in cogroo_sentence.getTokens():
            self.tokens.append(Token(token))

        self.chunks = []
        for chunk in cogroo_sentence.getChunks():
            self.chunks.append(Chunk(self, chunk))

        self.synchunks = []
        for synchunk in cogroo_sentence.getSyntacticChunks():
            self.synchunks.append(Chunk(self, synchunk))

    def __repr__(self):
        return self.text


class Document:
    def __init__(self, cogroo_doc: CogrooDocument):
        self.text = cogroo_doc.getText()

        paragraphs_ind = find('\n', cogroo_doc.getText())
        paragraph = 1
        last_sent_end = -1

        self.sentences = []
        for sentence in cogroo_doc.getSentences():
            if len(paragraphs_ind) > 0:
                start, end = paragraphs_ind[0]
                if start <= last_sent_end and last_sent_end != -1:
                    del paragraphs_ind[0]
                    paragraph += 1

            self.sentences.append(Sentence(sentence, paragraph))
            last_sent_end = sentence.getEnd()


        self.paragraphs = []
        for sentence in self.sentences:
            p = sentence.paragraph
            if len(self.paragraphs) < p:
                self.paragraphs.append([])

            self.paragraphs[-1].append(sentence)

        if cogroo_doc.getClass().getSimpleName() == 'CheckDocument':
            self.mistakes = []
            for cogroo_mistake in cogroo_doc.getMistakes():
                self.mistakes.append(Mistake(cogroo_mistake))


    def __repr__(self):
        return self.text


class Mistake:

    def __init__(self, cogroo_mistake):
        self.rule_id = cogroo_mistake.getRuleIdentifier()
        self.short_msg = cogroo_mistake.getShortMessage()
        self.long_msg = cogroo_mistake.getLongMessage()
        self.full_msg = cogroo_mistake.getFullMessage()
        suggestions = cogroo_mistake.getSuggestions()
        self.suggestions = [s for s in suggestions]
        self.start = cogroo_mistake.getStart()
        self.end = cogroo_mistake.getEnd()
        self.context = cogroo_mistake.getContext()
        self.rule_priority = cogroo_mistake.getRulePriority()

    def __repr__(self):
        return '[{0}] {1}'.format(self.rule_id, self.short_msg)


class Cogroo:
    _analyzer = None

    @property
    def analyzer(self) -> CogrooAnalyzer:
        if not self._analyzer:
            self._analyzer = CogrooAnalyzer()
        return self._analyzer

    @staticmethod
    def Instance():
        return Cogroo()

    @lru_cache(maxsize=5000)
    def analyze(self, text):
        text = self._preproc(text)
        try:
            doc = self.analyzer.analyze(text)
        except:
            try:
                #TODO check this workaround for better solution
                text = re.sub(', e a', ', E a', text)
                doc = self.analyzer.analyze(text)
            except:
                LOGGER.error('Couldn\'t connect with CoGrOO. Is it running?')
                return None

        return Document(doc)

    def grammar_check(self, text):
        text = self._preproc(text)
        doc = None
        try:
            doc = self.analyzer.grammarCheck(text)
        except:			
            LOGGER.error('Couldn\'t connect with CoGrOO for grammar check. Is it running?')
            return None

        return Document(doc)

    def _preproc(self, text):
        # Trim sentences
        text = re.sub('[ ]+\n', '', text)
        # Add missing final dots
        text = re.sub(r'([^.?!])\n', r'\1.\n', text)
        # Add missing spaces
        text = re.sub(r'([?!.,:;])(\S)', r'\1 \2', text)
        return text

    def lemmatize(self, text):
        if text is None or text == '':
            return ''

        if type(text) is not Document:
            doc = self.analyze(text)
        else:
            doc = text

        if doc is None:
            return ''

        ret = []
        last_paragraph = -1
        for sentence in doc.sentences:
            if sentence.paragraph > last_paragraph and last_paragraph != -1:
                ret.append('\n')

            for token in sentence.tokens:
                ret.append(token.lemma)

            last_paragraph = sentence.paragraph


        return ' '.join(ret)


    def pos_tag(self, text):
        if text is None or text == '':
            return ''

        if type(text) is not Document:
            doc = self.analyze(text)
        else:
            doc = text

        if doc is None:
            return ''

        ret = []
        for sentence in doc.sentences:
            for token in sentence.tokens:
                ret.append(token.lexeme + '#' + token.pos)

        return ' '.join(ret)


    def chunk_tag(self, text, type_='normal'):
        if text is None or text == '':
            return ''

        if type(text) is not Document:
            doc = self.analyze(text)
        else:
            doc = text

        if doc is None:
            return ''

        ret = []
        for sentence in doc.sentences:
            if type_ == 'normal':
                chunks = sentence.chunks
            else:
                chunks = sentence.synchunks

            for chunk in chunks:
                tokens = []
                for token in chunk.tokens:
                    tokens.append(token.lexeme)

                ret.append(chunk.tag + '[' + ' '.join(tokens) + ']')

        return ' '.join(ret)

    pos_tags = {
        "n": "substantivo",
        "prop": "nome próprio",
        "art": "artigo",
        "pron": "pronome",
        "pron-pers": "pronome pessoal",
        "pron-det": "pronome determinativo",
        "pron-indp": "substantivo/pron-indp",
        "n-adj": "substantivo/adjetivo",
        "v": "verbo",
        "v-fin": "verbo finitivo",
        "v-inf": "verbo infinitivo",
        "v-pcp": "verbo particípio",
        "v-ger": "verbo gerúndio",
        "num": "numeral",
        "prp": "preposição",
        "adj": "adjetivo",
        "conj": "conjunção",
        "conj-s": "conjunção subordinativa",
        "conj-c": "conjunção coordenativa",
        "intj": "interjeição",
        "adv": "advérbio",
        "xxx": "outro"}

    feat_tags = {
        "M": "masculino",
        "F": "feminino",
        "M/F": "masculino/feminino",

        "S": "singular",
        "P": "plural",

        "NOM": "nominativo",
        "ACC": "acusativo",
        "DAT": "dativo",
        "PIV": "prepositivo",

        "1": "primeira pessoa",
        "2": "segunda pessoa",
        "3": "terceira pessoa",

        "1S": "primeira pessoa singular",
        "2S": "segunda pessoa singular",
        "3S": "terceira pessoa singular",
        "1P": "primeira pessoa plural",
        "2P": "segunda pessoa plural",
        "3P": "terceira pessoa plural",

        "PR": "presente",
        "IMPF": "imperfeito",
        "PS": "perfeito simples",
        "MQP": "mais-que-perfeito",
        "FUT": "futuro",
        "COND": "condicional",

        "IND": "indicativo",
        "SUBJ": "subjuntivo",
        "IMP": "imperativo",

        "xxx": "outro"
    }

    chunk_tags = {
        "NP": "nominal",
        "VP": "verbal",
        "PP": "preposicional",
        "ADVP": "adverbial",
        "xxx": "outro"
    }

    synchunk_tags = {
        "ACC": "objeto direto",
        "ADVL": "adjunto adverbial",
        "APP": "aposição",
        "DAT": "objeto indireto pronominal",
        "OC": "predicativo do objeto",
        "P": "predicado",
        "PIV": "objeto preposicional",
        "SA": "complemento adverbial",
        "SC": "predicativo do sujeito",
        "SUBJ": "sujeito",
        "xxx": "outro"
    }


def main():
    cogroo = Cogroo.Instance()
    print(cogroo.lemmatize('o entendimento das metas propostas oferece uma interessante oportunidade para ' +
                           'verificação do impacto na agilidade decisória'))


if __name__ == '__main__':
    main()