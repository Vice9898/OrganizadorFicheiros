# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:25:02 2026

@author: diogo
"""

from pathlib import Path

pasta = Path.cwd()

contagem = 0

print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")

for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        contagem += 1

        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)

        if ficheiro.suffix == ".py":
            print("Tipo: Ficheiro Python")

        elif ficheiro.suffix == ".txt":
            print("Tipo: Ficheiro de texto")

        elif ficheiro.suffix == ".csv":
            print("Tipo: Ficheiro CSV")

        print("-----------------------")

if contagem == 0:
    print("A pasta não contém ficheiros.")

else:
    print("Total de ficheiros encontrados:", contagem)
