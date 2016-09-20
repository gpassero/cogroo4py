# CoGrOO4Py
Uma interface para acessar o analisador morfológico do CoGrOO em Python.

# Pré-requisitos
 - interpretador Python v 3.*
 - Pacote py4j (pip install py4j)
 - Java Runtime Environment v 8+

# Como usar
Baixe os arquivos cogroo_interface.py e setup.py e instale o pacote com o comando:

    python setup.py install

Se preferir, instale a partir do GitHub pelo pip:

    pip install git+https://github.com/gpassero/cogroo4py.git

É necessário executar o arquivo cogroo4py.jar para ativar o Socket que permitirá a comunicação do Python com a JVM através do py4j. Todos os componentes do CoGrOO necessários (v 4) já estão nesse pacote.

    java -jar cogroo4py.jar
    Gateway Server Started

Após isso, em uma IDE Python de sua preferência (ex. IPython, Spyder), importe e instancie a classe Cogroo.

    from cogroo_interface import Cogroo
    cogroo = Cogroo.Instance()

Agora você já pode usar os recursos do CoGrOO. Esta interface disponibiliza atualmente métodos para retornar uma análise morfológica completa de um documento, lematizar, identificar partes do discurso e dividir em chunks. 

Abaixo estão alguns exemplos de uso:

    cogroo.lemmatize('Estas laranjas estão deliciosas.')
      este laranja estar delicioso.
      
    doc = cogroo.analyze('Estas laranjas estão deliciosas.')
    doc.sentences[0].tokens
      [Estas#pron-det F=P,
       laranjas#n F=P,
       estão#v-fin PR=3P=IND,
       deliciosas#adj F=P,
       .#. -]
       
    doc = cogroo.chunk_tag('Estas laranjas estão deliciosas.')
      'NP[Estas laranjas esto deliciosas]'
 
