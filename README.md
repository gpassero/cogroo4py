# CoGrOO4Py
[![Build Status](https://travis-ci.org/kevencarneiro/cogroo4py.svg?branch=master)](https://travis-ci.org/kevencarneiro/cogroo4py)
[![codecov](https://codecov.io/gh/kevencarneiro/cogroo4py/branch/master/graph/badge.svg)](https://codecov.io/gh/kevencarneiro/cogroo4py)
[![PyPI version](https://badge.fury.io/py/cogroo-interface.svg)](https://badge.fury.io/py/cogroo-interface)

Uma interface para acessar o analisador morfológico e o corretor gramatical do CoGrOO em Python.

# Pré-requisitos
 - interpretador Python 3.x
 - Java Runtime Environment 8

# Como usar
Instale usando o pip:

```
    pip install cogroo_interface
```

É necessário que o executável `java` esteja definido em seu `path`

Em uma IDE Python de sua preferência (ex. IPython, Spyder), importe e instancie a classe *Cogroo*.

```python
    from cogroo_interface import Cogroo
    cogroo = Cogroo.Instance()
```

Agora você já pode usar os recursos do CoGrOO. Esta interface disponibiliza métodos para retornar uma análise morfológica completa de um documento, lematizar, identificar partes do discurso, dividir em chunks e verificar erros gramaticais. 

## Lematizando
A lematização consiste em obter o lema das palavras de um texto. O lema é uma versão da palavra que representa todas as suas flexões. Os verbos são alterados para o infinitivo e substantivos e adjetivos são flexionados para o masculino do singular.

		[estava, estaria, estive, estarei, estar] => estar
		[fui, vou, ire, iremos] => ir
		[gato, gatinho, gatão, gata, gatos] => gato

A lematização é uma alternativa ao *stemming*, um algoritmo que tenta detectar sufixos e removê-los com base nas regras comuns da língua, mas que falha em tratar exceções. A lematização, diferentemente do *stemming*, usa um dicionário morfológico para encontrar o radical das palavras.

```python
    cogroo.lemmatize('Estas laranjas estão deliciosas.')
    # este laranja estar delicioso.
```

## Análise morfológica
A análise morfológica consiste em identificar a classe gramatical das palavras de um texto. As classes possíveis são: substantivos, adjetivos, artigos, pronomes, numeral, verbo, advérbio, preposição, conjunção e interjeição.

O método de análise morfológica do CoGrOO usa etiquetas (*tags*) específicas para cada caso, que podem ser difíceis de entender em um primeiro momento. O dicionário *pos_tags* da classe **Cogroo** permite traduzir as etiquetas geradas pelo CoGrOO para um formato legível em português:

```python
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
	
	# pos: "part of speech"
	pos = cogroo.pos_tags
	pos['n']
	# substantivo
```

No contexto de Processamento de Linguagem Natural as palavras e caracteres de pontuação são normalmente tratados como *tokens*. O método *analyze* associa uma das etiquetas acima para cada *token* de um texto. Também são anotadas algumas *features* que indicam a flexão das palavras, ex. **F=P => *feminino, plural***.

```python
    doc = cogroo.analyze('Estas laranjas estão deliciosas.')
    doc.sentences[0].tokens
    #  [Estas#pron-det F=P,
    #   laranjas#n F=P,
    #   estão#v-fin PR=3P=IND,
    #   deliciosas#adj F=P,
    #   .#. -]
 ```
 
## Corretor gramatical
O corretor gramatical do CoGrOO verifica a colocação pronominal, concordância nominal, concordância entre sujeito e verbo, concordância verbal, uso de crase, regência nominal, regência verbal e outros erros comuns da língua portuguesa escrita. Mais detalhes sobre as regras aplicadas podem ser encontrados em http://comunidade.cogroo.org/rules.

```python
    doc = cogroo.grammar_check('Elas são bonita.')
	doc.mistakes
	# [[xml:124] O adjetivo na função de predicativo concorda com o sujeito.]
```

# Sobre o CoGrOO 
Código fonte e informações sobre o projeto:
http://cogroo.sourceforge.net/
https://github.com/cogroo/cogroo4

Demonstração online
http://comunidade.cogroo.org/grammar

Dissertação de mestrado sobre o desenvolvimento do CoGrOO 4
http://www.teses.usp.br/teses/disponiveis/45/45134/tde-02052013-135414/pt-br.php
