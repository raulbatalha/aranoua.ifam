#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:18:37 2023

@author: Raul Batalha

(Questão - 05) - Elabore um programa para ler o código de um banco e mostrar o nome, conforme a tabela abaixo:

+-----------------------+-------------------------+
| Código                | Banco                   |
+-----------------------+-------------------------+
| 1                     | Banco do Brasil         |
| 33                    | Santander               |
| 104                   | Caixa Econômica Federal |
| 237                   | Bradesco                |
| Qualquer outro código | Banco não identificado  |
+-----------------------+-------------------------+

"""


class Banco:
    @staticmethod
    def obter_nome_banco(codigo):
        bancos = {
            1: "Banco do Brasil",
            33: "Santander",
            104: "Caixa Econômica Federal",
            237: "Bradesco"
        }

        return bancos.get(codigo, "Banco não identificado")

    @staticmethod
    def menu_obter_nome_banco():
        try:
            codigo_banco = int(input("Digite o código do banco: "))
            nome_banco = Banco.obter_nome_banco(codigo_banco)
            print(f"Nome do banco: {nome_banco}")
        except ValueError:
            print("Código inválido. Digite um número válido.")
