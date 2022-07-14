#!/usr/bin/env python3
""" Bloco de Notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print(f'Invalid command {argument[0]}')

if arguments[0] == 'read':
    # leitura das notas
    searchtype, keyword = arguments[1].split("=")
    searchtype = searchtype.lstrip("-").strip().lower()
    keyword = keyword.strip().lower()
    result = []
    with open(filepath) as file:
        for line in file:
            if "*" in line:
                content = line.split("*")
                if searchtype == "tag" and keyword == content[1].lower():
                    print(content[2])      

if arguments[0] == 'new':
    # criação da nota
    if not arguments[1]:
        title = input("Insert note title: ")
    else:
        title = arguments[1]
    tag = input("tag: ")
    text = input("text: ")
    with open(filepath, "a") as file:
        #for key, value in note.items():
           # file.writelines(f'{key}:{value}\n')
        file.writelines(f'\n{title}*{tag}*{text}')
         
