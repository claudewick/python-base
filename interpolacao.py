#!/usr/bin/env python
""" Imprime a mensagem de um email

NÃO MANDE SPAM
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)
clientes = []
for line in open(filename):
    name, email = line.split(",")
    #TODO substituir por envio de email
    print(f'Enviando email para: {email}')
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
