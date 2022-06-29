#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e:
    print(f'{str(e)}')
    sys.exit(1)
    # TODO: usar retry
else:
    print("Sucesso") #só executa se não executar o except
finally:
    print("execute isso sempre") # executa sempre

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
