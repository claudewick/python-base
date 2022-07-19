#!/usr/bin/env python3
"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o 
índice de umidade do ar sendo que caso será exibida uma mensagem de 
alerta dependendo das condições.

temp maior 45: ALERTA!!! Perigo calor extremo
temp maior que 30 e temp vezes 3 for maior ou igual a umidade: 
ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0: ALERTA: Frio extremo
"""

temp = float(input("Informe a temperatura: "))
umidade = float(input("Informe a umidade: "))

if temp < 0:
    msg = "ALERTA: Frio extremo"
elif 0 <= temp < 10:
    msg = "Frio"
elif 10 <= temp < 30:
    msg = "Normal"
elif temp > 45:
    msg = "ALERTA!!! Perigo calor extremo"
elif (temp * 3) <= umidade and temp > 30:
    msg = "ALERTA!!! Perigo de calor úmido" 
else:
    msg ="Está calor né, será que vai chover?"

print(msg)
