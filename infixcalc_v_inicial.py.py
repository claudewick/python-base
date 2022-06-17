#!/usr/bin/env python3
""" Calculadora infix

Funcionamento:

[operação] [n1] [n2]

Operações: 
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

argumentos = {"operação": None, "n1": None, "n2": None}
operacoes = ("sum", "sub", "mul", "div")

if len(sys.argv) > 1 and sys.argv[1] in operacoes:
    argumentos["operação"] = sys.argv[1].strip()
    # TODO: Tratar ausência dos demais argumentos *list index out of range*
    argumentos["n1"] = sys.argv[2].strip()
    # TODO: Tratar divisão por zero
    argumentos["n2"] = sys.argv[3].strip()
else:
    argumentos["operação"] = input("Operação:").strip()
    if argumentos["operação"] not in operacoes:
        print('Opção inválida')
        sys.exit()
    else:
        argumentos["n1"] = input("n1:").strip()
        argumentos["n2"] = input("n2:").strip()

operacao = argumentos["operação"]
n1 = float(argumentos["n1"])
n2 = float(argumentos["n2"])

if operacao == "sum":
    resultado = n1 + n2
elif operacao == "sub":
    resultado = n1 - n2
elif operacao == "mul":
    resultado = n1 * n2
elif operacao == "div":
    resultado = n1 / n2

print(resultado)