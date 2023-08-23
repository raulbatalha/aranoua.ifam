#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:00:42 2023

@author: Raul Batalha

(Questão - 01) - Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço
normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

+--------+-----------------------------------------------------------+
| Código | Condição de Pagamento                                     |
+--------+-----------------------------------------------------------+
| 1      | À vista em dinheiro ou cheque, recebe 10% de desconto     |
| 2      | À vista no cartão de crédito, recebe 15% de desconto      |
| 3      | Em duas vezes, preço normal de etiqueta sem juros         |
| 4      | Em duas vezes, preço normal de etiqueta mais juros de 10% |
+--------+-----------------------------------------------------------+

"""


class Pagamento:
    @staticmethod
    def calcular_valor_pagamento(preco_etiqueta, codigo_condicao):
        if codigo_condicao == 1:
            desconto = 0.1
            valor_pago = preco_etiqueta - (preco_etiqueta * desconto)
        elif codigo_condicao == 2:
            desconto = 0.15
            valor_pago = preco_etiqueta - (preco_etiqueta * desconto)
        elif codigo_condicao == 3:
            valor_pago = preco_etiqueta
        elif codigo_condicao == 4:
            juros = 0.1
            valor_pago = preco_etiqueta + (preco_etiqueta * juros)
        else:
            print("Condição de pagamento inválida.")
            return None
        return valor_pago

    @staticmethod
    def menu_pagamento():
        preco_etiqueta = float(
            input("Digite o preço da etiqueta do produto R$: "))

        print("Opções de pagamento:")
        print("1 - À vista em dinheiro ou cheque, recebe 10 % de desconto")
        print("2 - À vista no cartão de crédito, recebe 15% de desconto")
        print("3 - Em duas vezes, preço normal de etiqueta sem juros")
        print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10%")

        condicao_de_pagamento = int(
            input("Escolha a opção de pagamento (1/2/3/4): "))

        valor_pago = Pagamento.calcular_valor_pagamento(
            preco_etiqueta, condicao_de_pagamento)

        if valor_pago is not None:
            print(f"Valor a ser pago: R$ {valor_pago:.2f}")
