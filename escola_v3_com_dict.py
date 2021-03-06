#!/usr/bin/env python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]


atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for chave, valor in atividades.items():
    
    print(f"Alunos da atividade {chave}\n")
    print("-" * 50)
    
    atividade_sala1 = []
    atividade_sala2 = []
    
    for aluno in valor:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    
        
    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print()
    print("#" * 50)