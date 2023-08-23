#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:08:52 2023

@author: Raul Batalha


(Questão - 02) - O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura) 2
Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
com a tabela abaixo:

+---------------+----------------+
| IMC           | Condição       |
+---------------+----------------+
| <18.5         | Abaixo do Peso |
| >=18.5 e <=25 | Peso Normal    |
| >25 e <=30    | Acima do Peso  |
| >30           | Obeso          |
+---------------+----------------+

"""


class CalculadoraIMC:
    @staticmethod
    def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        return imc

    @staticmethod
    def determinar_condicao(imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc <= 25:
            return "Peso normal"
        elif 25 < imc <= 30:
            return "Acima do peso"
        else:
            return "Obeso"

    @staticmethod
    def menu_imc():
        peso_str = input("Digite o peso (em kg): ").replace(',', '.')
        altura = float(input("Digite a altura (em metros): "))

        peso = float(peso_str)

        imc = CalculadoraIMC.calcular_imc(peso, altura)

        condicao = CalculadoraIMC.determinar_condicao(imc)
        print(
            f"Seu IMC é {imc:.2f}, e você está classificado como '{condicao}'.")