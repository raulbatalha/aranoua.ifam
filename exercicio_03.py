#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:15:26 2023

@author: Raul Batalha

(Questão - 03) - Desenvolva um algoritmo para identificar letras, números, pontuações “?”, “!”, “.”, “;” e “,”. Caso não se
encaixe em nenhum desses, informe que é um “Caractere especial”.

"""


class IdentificadorCaractere:
    @staticmethod
    def identificar_caractere(caractere):
        if caractere.isalpha():
            return "Letra"
        elif caractere.isdigit():
            return "Número"
        elif caractere in ["?", "!", ".", ";", ","]:
            return "Pontuação"
        else:
            return "Caractere especial"

    @staticmethod
    def menu_identificar_caractere():
        caractere = input("Digite um caractere: ")
        for c in caractere:
            resultado = IdentificadorCaractere.identificar_caractere(c)
            print(f"O caractere '{c}' é classificado como: {resultado}")
