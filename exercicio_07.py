#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:22:57 2023

@author: raulbatalha

(Questão - 07) - A Alíquota do cálculo mensal do imposto de renda 2023 é baseada na tabela abaixo:

+---------------------------------+--------------+
| Base de Cálculo (Salário em R$) | Alíquota (%) |
+---------------------------------+--------------+
| Até R$ 1.903,98                 | 0,0          |
| De R$ 1.903,99 a R$ 2.826,65    | 7,5          |
| De R$ 2.826,66 a R$ 3.751,05    | 15,0         |
| De R$ 3.751,06 a R$ 4.664,68    | 22,5         |
| Acima de R$ 4.664,68            | 27,5         |
+---------------------------------+--------------+

Crie um algoritmo para ler o salário, calcular a alíquota e mostrar o valor do Imposto de
Renda mensal.

"""


class CalculadoraImpostoRenda:
    @staticmethod
    def calcular_imposto_renda(salario):
        if salario <= 1903.98:
            aliquota = 0.0
        elif salario <= 2826.65:
            aliquota = 7.5
        elif salario <= 3751.05:
            aliquota = 15.0
        elif salario <= 4664.68:
            aliquota = 22.5
        else:
            aliquota = 27.5

        imposto_renda = salario * (aliquota / 100)
        return imposto_renda

    @staticmethod
    def menu_calcular_imposto_renda():
        try:
            salario_str = input("Digite o salário em R$: ").replace(
                '.', '').replace(',', '.')
            salario = float(salario_str)

            imposto_renda_mensal = CalculadoraImpostoRenda.calcular_imposto_renda(
                salario)
            print(
                f"O valor do Imposto de Renda mensal é: R$ {imposto_renda_mensal:.2f}")
        except ValueError:
            print("Valor de salário inválido. Certifique-se de digitar um número válido.")
