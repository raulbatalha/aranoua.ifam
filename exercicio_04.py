#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:12:38 2023

@author: Raul Batalha

(Questão - 04) - Elabore um programa para ler um número Natural (0 a 9) e mostrar o número por extenso.

"""


class NumeroPorExtenso:
    @staticmethod
    def mostrar_numero_extenso(numero):
        numeros_extenso = {
            0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro",
            5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"
        }

        if numero in numeros_extenso:
            return numeros_extenso[numero]
        else:
            return "Número fora do intervalo válido."

    @staticmethod
    def menu_numero_extenso():
        try:
            numero = int(input("Digite um número natural (0 a 9): "))
            if 0 <= numero <= 9:
                numero_extenso = NumeroPorExtenso.mostrar_numero_extenso(
                    numero)
                print(f"O número {numero} por extenso é: {numero_extenso}")
            else:
                print("Número fora do intervalo válido.")
        except ValueError:
            print("Entrada inválida. Digite um número natural (0 a 9).")