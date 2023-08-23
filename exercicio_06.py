#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:19:44 2023

@author: Raul Batalha

(Questão - 06) - Faça um programa que leia o ano de nascimento de nascimento de uma pessoa, calcule e mostre sua
idade em relação ao ano corrente (2023) e, também, verifique e mostre se a ela já tem idade para votar
e para tirar a carteira de habilitação.

"""

from datetime import datetime


class VerificadorIdade:
    @staticmethod
    def calcular_idade(ano_nascimento):
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento
        return idade

    @staticmethod
    def verificar_voto_e_habilitacao(idade):
        if 16 <= idade < 18 or idade >= 70:
            return "Voto facultativo"
        elif 18 <= idade < 70:
            return "Voto obrigatório e possível obtenção de habilitação"
        else:
            return "Não possui idade para votar ou obter habilitação"

    @staticmethod
    def menu_verificar_idade():
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            idade = VerificadorIdade.calcular_idade(ano_nascimento)

            print(f"Idade: {idade} anos")
            print(VerificadorIdade.verificar_voto_e_habilitacao(idade))

            if 16 <= idade < 18:
                meses_faltantes_para_habilitacao = 18 - idade
                if meses_faltantes_para_habilitacao > 0:
                    print(
                        f"Faltam {meses_faltantes_para_habilitacao} anos para poder obter a habilitação.")
                else:
                    print("Você já pode obter a habilitação!")

        except ValueError:
            print(
                "Ano de nascimento inválido. Certifique-se de digitar um número inteiro.")
