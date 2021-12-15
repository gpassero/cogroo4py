# CoGrOO4Py
[![Build Status](https://github.com/kevencarneiro/cogroo4py/actions/workflows/main.yml/badge.svg)](https://github.com/kevencarneiro/cogroo4py/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/kevencarneiro/cogroo4py/branch/master/graph/badge.svg)](https://codecov.io/gh/kevencarneiro/cogroo4py)
[![PyPI version](https://badge.fury.io/py/cogroo4py.svg)](https://badge.fury.io/py/cogroo4py)

Uma interface para acessar o analisador morfológico e o corretor gramatical do CoGrOO em Python.

# Pré-requisitos
 - interpretador Python 3.x
 - Java Runtime Environment (Testado nas versões 8, 11 e 17)

# Como usar
Instale usando o pip:

```
    pip install cogroo4py
```

É necessário que o executável `java` esteja definido em seu `path`

Em uma IDE Python de sua preferência (ex. IPython, Spyder), importe e instancie a classe *Cogroo*.

```python
    from cogroo4py.cogroo import Cogroo
    cogroo = Cogroo()
```

Agora você já pode usar os recursos do CoGrOO. Esta interface disponibiliza métodos para retornar uma análise morfológica completa de um documento, lematizar, identificar partes do discurso, dividir em chunks e verificar erros gramaticais.

## Lematizando

A lematização consiste em obter o lema das palavras de um texto. O lema é uma versão da palavra que representa todas as suas flexões. Os verbos são alterados para o infinitivo e substantivos e adjetivos são flexionados para o masculino do singular.

    	[estava, estaria, estive, estarei, estar] => estar
    	[fui, vou, irei, iremos] => ir
    	[gato, gatinho, gatão, gata, gatos] => gato

A lematização é uma alternativa ao _stemming_, um algoritmo que tenta detectar sufixos e removê-los com base nas regras comuns da língua, mas que falha em tratar exceções. A lematização, diferentemente do _stemming_, usa um dicionário morfológico para encontrar o radical das palavras.

```python
    cogroo.lemmatize('Estas laranjas estão deliciosas.')
    # este laranja estar delicioso.
```

## Análise morfológica

A análise morfológica consiste em identificar a classe gramatical das palavras de um texto. As classes possíveis são: substantivos, adjetivos, artigos, pronomes, numeral, verbo, advérbio, preposição, conjunção e interjeição.

O método de análise morfológica do CoGrOO usa etiquetas (_tags_) específicas para cada caso, que podem ser difíceis de entender em um primeiro momento. O dicionário _pos_tags_ da classe **Cogroo** permite traduzir as etiquetas geradas pelo CoGrOO para um formato legível em português:

```python
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
        "xxx": "outro"
    }
	
	# pos: "part of speech"
	pos = cogroo.pos_tags
	pos['n']
	# substantivo
```

No contexto de Processamento de Linguagem Natural as palavras e caracteres de pontuação são normalmente tratados como _tokens_. O método _analyze_ associa uma das etiquetas acima para cada _token_ de um texto. Também são anotadas algumas _features_ que indicam a flexão das palavras, ex. **F=P => _feminino, plural_**.

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

# Contribuindo

Este projeto utiliza o jpype para se comunicar com a Java Native Interface (JNI) e utilizar as classes do Cogroo

Requirements:
* Java (compilado na versão 8, porém os testes unitários rodam entre a versão 8 e 17 do JDK)

## Configuração do ambiente de desenvolvimento
* É recomendável utilizar um virtual environment (venv)
* Na raiz do projeto python, execute o comando `pip install -e .[dev]`

## Atualizando as dependências do Java
* `cd java`
* `mvn package`

Este comando irá atualizar o arquivo `/python/cogroo4py/jars/Cogroo4PyBridge.jar`

## Regerando os stubs python
* `cd python/cogroo4py`
* `python generate_stubs.py`

Os stubs servirão para o autocomplete das classes Java utilizadas dentro do python

# Sobre o CoGrOO 
Código fonte e informações sobre o projeto:
http://cogroo.sourceforge.net/
https://github.com/cogroo/cogroo4

Demonstração online
http://comunidade.cogroo.org/grammar

Dissertação de mestrado sobre o desenvolvimento do CoGrOO 4
http://www.teses.usp.br/teses/disponiveis/45/45134/tde-02052013-135414/pt-br.php
