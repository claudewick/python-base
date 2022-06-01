#!/c/Users/claud/AppData/Local/Programs/Python/Python39/python (este é um SHEBANG usado apenas em scripts para indicar qual a versão do Python que ele deve rodar)
""" Hello World Multi Linguas.

Dependendo da língua configurada no ambiente oprograma exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG configurada ex:
    
    export LANG=pt_BR
    
Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = '0.1.2'
__author__ = 'Claude Wickihalder'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'en_US': 'Hello, World!',
    'pt_BR': 'Olá, Mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour Monde',
}

print(msg[current_language])