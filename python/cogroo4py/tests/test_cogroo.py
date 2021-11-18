# -*- coding: utf-8 -*-
import unittest
from cogroo4py.cogroo import Cogroo

class TestCogroo(unittest.TestCase):
    def test_lemmatize(self):
        cogroo = Cogroo()
        phrase_to_lemmatize = 'o entendimento das metas propostas oferece uma interessante oportunidade para verificação ' \
                            'do impacto na agilidade decisória '
        expected_result = 'o entender de o meta propor oferecer um interessante oportunidade para verificação de o ' \
                        'impacto em o agilidade decisório'
        self.assertEqual(expected_result, cogroo.lemmatize(phrase_to_lemmatize))

    def test_mistakes():
        cogroo = Cogroo()
        doc = cogroo.grammar_check('Elas são bonita')
        self.assertTrue(doc.mistakes)
