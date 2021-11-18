# -*- coding: utf-8 -*-
from cogroo4py.cogroo import Cogroo


def test_lemmatize():
    cogroo = Cogroo.Instance()
    phrase_to_lemmatize = 'o entendimento das metas propostas oferece uma interessante oportunidade para verificação ' \
                          'do impacto na agilidade decisória '
    expected_result = 'o entender de o meta propor oferecer um interessante oportunidade para verificação de o ' \
                      'impacto em o agilidade decisório'
    assert expected_result == cogroo.lemmatize(phrase_to_lemmatize)