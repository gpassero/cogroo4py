# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 21:21:19 2016

@author: Guilherme Passero <guilherme.passero0@gmail.com>
"""
from py4j.java_gateway import JavaGateway
from functools import lru_cache
import logging
import re


LOGGER = logging.getLogger(__name__)


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


def find(pattern, text):
    return [(i.start(), i.end()) for i in re.finditer(pattern, text)]


class Token:
    def __init__(self, cogroo_token):
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
    def __init__(self, sentence, cogroo_chunk):
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
    def __init__(self, cogroo_sentence, paragraph):
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
    def __init__(self, cogroo_doc):
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


@Singleton
class Cogroo:

    def __init__(self):
        self.gateway = JavaGateway()
        self.analyzer = self.gateway.entry_point
        self.pos_tags = self._pos_tags()
        self.feat_tags = self._feat_tags()
        self.chunk_tags = self._chunk_tags()
        self.synchunk_tags = self._synchunk_tags()

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

    def _pos_tags(self):
        pos = {}
        pos.update({"n": "substantivo"})
        pos.update({"prop": "nome próprio"})
        pos.update({"art": "artigo"})
        pos.update({"pron": "pronome"})
        pos.update({"pron-pers": "pronome pessoal"})
        pos.update({"pron-det": "pronome determinativo"})
        pos.update({"pron-indp": "substantivo/pron-indp"})
        pos.update({"adj": "adjetivo"})
        pos.update({"n-adj": "substantivo/adjetivo"})
        pos.update({"v": "verbo"})
        pos.update({"v-fin": "verbo finitivo"})
        pos.update({"v-inf": "verbo infinitivo"})
        pos.update({"v-pcp": "verbo particípio"})
        pos.update({"v-ger": "verbo gerúndio"})
        pos.update({"num": "numeral"})
        pos.update({"prp": "preposição"})
        pos.update({"adj": "adjetivo"})
        pos.update({"conj": "conjunção"})
        pos.update({"conj-s": "conjunção subordinativa"})
        pos.update({"conj-c": "conjunção coordenativa"})
        pos.update({"intj": "interjeição"})
        pos.update({"adv": "advérbio"})
        pos.update({"xxx": "outro"})
        return pos

    def _feat_tags(self):
        feat = {}

        feat.update({"M": "masculino"})
        feat.update({"F": "feminino"})
        feat.update({"M/F": "masculino/feminino"})

        feat.update({"S": "singular"})
        feat.update({"P": "plural"})

        feat.update({"NOM": "nominativo"})
        feat.update({"ACC": "acusativo"})
        feat.update({"DAT": "dativo"})
        feat.update({"PIV": "prepositivo"})

        feat.update({"1": "primeira pessoa"})
        feat.update({"2": "segunda pessoa"})
        feat.update({"3": "terceira pessoa"})

        feat.update({"1S": "primeira pessoa singular"})
        feat.update({"2S": "segunda pessoa singular"})
        feat.update({"3S": "terceira pessoa singular"})
        feat.update({"1P": "primeira pessoa plural"})
        feat.update({"2P": "segunda pessoa plural"})
        feat.update({"3P": "terceira pessoa plural"})

        feat.update({"PR": "presente"})
        feat.update({"IMPF": "imperfeito"})
        feat.update({"PS": "perfeito simples"})
        feat.update({"MQP": "mais-que-perfeito"})
        feat.update({"FUT": "futuro"})
        feat.update({"COND": "condicional"})

        feat.update({"IND": "indicativo"})
        feat.update({"SUBJ": "subjuntivo"})
        feat.update({"IMP": "imperativo"})

        feat.update({"xxx": "outro"})

        return feat

    def _chunk_tags(self):
        chunk = {}
        chunk.update({"NP": "nominal"})
        chunk.update({"VP": "verbal"})
        chunk.update({"PP": "preposicional"})
        chunk.update({"ADVP": "adverbial"})
        chunk.update({"xxx": "outro"})
        return chunk

    def _synchunk_tags(self):
        synchunk = {}
        synchunk.update({"ACC": "objeto direto"})
        synchunk.update({"ADVL": "adjunto adverbial"})
        synchunk.update({"APP": "aposição"})
        synchunk.update({"DAT": "objeto indireto pronominal"})
        synchunk.update({"OC": "predicativo do objeto"})
        synchunk.update({"P": "predicado"})
        synchunk.update({"PIV": "objeto preposicional"})
        synchunk.update({"SA": "complemento adverbial"})
        synchunk.update({"SC": "predicativo do sujeito"})
        synchunk.update({"SUBJ": "sujeito"})
        synchunk.update({"xxx": "outro"})
        return synchunk


cogroo = Cogroo.Instance()