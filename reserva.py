#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por vírgulas.

'quartos.txt'
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reservas.txt'
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma 
mensagem informando que já está reservado.
"""
import os
import sys

path = os.curdir
filepath_rooms = os.path.join(path, "quartos.txt")
filepath_reserved = os.path.join(path, "reservas.txt")

reserved = []
room_price = {}

# Capturar os quatos já reservados:
for line in open(filepath_reserved):
    if "#" in line:
        continue
    else:
        guest, room_number, days = line.split(",")
        reserved.append(room_number)

# Imprime a lista de quartos
print("Quartos disponíveis: ")
print("Código   |         Nome           |     Preço R$       ")
for line in open(filepath_rooms):
    if "#" in line:
        continue
    else:
        code, room_name, price = line.split(",")
        room_price[code] = int(price)
        print(f'{code}        | {room_name}  | R$ {price}')

# captura a reserva do cliente
guest_name = input("Informe seu nome: ").strip()
room = input("Informe o código do quarto escolhido: ").strip()
days = input("Informe a quantidade de diárias: ").strip()

# Confere se o quarto está reservado
try:
    if room in reserved:
        print(f"Lamentamos, mas o quarto {room} já está reservado")
    else:
        print(f'O valor da sua reserva é R${int(days) * room_price[room]}')
        with open(filepath_reserved, "a") as file_:
            file_.write(f'{guest_name},{room},{days}\n')
        print("Sua reserva foi efetivada com sucesso")
except (ValueError, KeyError):
    print("As informações fornecidas não foram suficientes para concluir a reserva.")
    print("Tente novamente.")
    sys.exit()            
