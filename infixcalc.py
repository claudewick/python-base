#!/usr/bin/env python3
""" Calculadora infix
<<<<<<< HEAD
Funcionamento:
[operação] [n1] [n2]
=======

Funcionamento:

[operação] [n1] [n2]

>>>>>>> 5a4facd5a81720afdd0b95565ffcdcb203ab68de
Operações: 
sum -> +
sub -> -
mul -> *
div -> /
<<<<<<< HEAD
Uso:
$ infixcalc.py sum 5 2
7
$ infixcalc.py mul 10 5
50
=======

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

>>>>>>> 5a4facd5a81720afdd0b95565ffcdcb203ab68de
$ infixcalc.py 
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys
arguments = sys.argv[1:]

if not arguments:
    operation = input("operação:")
    n1 = input("n1")
    n2 = input("n2")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)

operation, *nums = arguments
valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []

for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
        
n1, n2 = validated_nums

# TODO: Usar dicionário de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

<<<<<<< HEAD
print(f'O resultado é {result}')
=======
print(f'O resultado é {result}')
>>>>>>> 5a4facd5a81720afdd0b95565ffcdcb203ab68de