#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex.:
python3 repete_vogal.py
'Digite uma palavra (ou ENTER para sair): ' Python
'Digite uma palavra (ou ENTER para sair): ' Bruno
'Digite uma palavra (ou ENTER para sair): ' <ENTER>
Pythoon
Bruunoo
"""

palavras = []

while True:
    palavra = input('Digite uma palavra (ou ENTER para sair): ').strip()
    if palavra:
        palavras.append(palavra) 
    else:
        break

for palavra in palavras:
    nova_palavra = ""
    for letra in palavra:
        if letra not in "aeiou":
            nova_palavra += letra
        else:
            nova_palavra += letra * 2
    print(nova_palavra)
