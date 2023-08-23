#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:29:12 2023

@author: Raul Batalha

Instituto Federal de Educação, Ciência e Tecnologia do Amazonas - Campus Zona Leste
Especialização em Aprendizado de Máquina – Introdução à Programação
              
Prof⁰ Joethe Carvalho

Lista de Exercícios 1 – Estruturas de Seleção

"""
import sys
from exercicio_01 import Pagamento
from exercicio_02 import CalculadoraIMC
from exercicio_03 import IdentificadorCaractere
from exercicio_04 import NumeroPorExtenso
from exercicio_05 import Banco
from exercicio_06 import VerificadorIdade
from exercicio_07 import CalculadoraImpostoRenda


class MenuAtividades:
    def __init__(self):
        self.opcoes = {
            '1': self.menu_pagamento,
            '2': self.menu_imc,
            '3': self.menu_identificar_caractere,
            '4': self.menu_numero_extenso,
            '5': self.menu_obter_nome_banco,
            '6': self.menu_verificar_idade,
            '7': self.menu_calcular_imposto_renda,
            '0': self.sair
        }

    def mostrar_menu(self):
        while True:
            self.exibir_opcoes()
            opcao_escolhida = input("Escolha uma opção: ")

            if opcao_escolhida in self.opcoes:
                self.opcoes[opcao_escolhida]()
            else:
                print("Opção inválida. Escolha novamente.")

    def exibir_opcoes(self):
        print("Menu de Atividades:")
        print("1. Questão 1")
        print("2. Questão 2")
        print("3. Questão 3")
        print("4. Questão 4")
        print("5. Questão 5")
        print("6. Questão 6")
        print("7. Questão 7")
        print("0. Sair")

    def menu_pagamento(self):
        Pagamento.menu_pagamento()

    def menu_imc(self):
        CalculadoraIMC.menu_imc()

    def menu_identificar_caractere(self):
        IdentificadorCaractere.menu_identificar_caractere()

    def menu_numero_extenso(self):
        NumeroPorExtenso.menu_numero_extenso()

    def menu_obter_nome_banco(self):
        Banco.menu_obter_nome_banco()

    def menu_verificar_idade(self):
        VerificadorIdade.menu_verificar_idade()

    def menu_calcular_imposto_renda(self):
        CalculadoraImpostoRenda.menu_calcular_imposto_renda()

    @staticmethod
    def sair():
        print("Saindo do programa!")
        sys.exit()


if __name__ == "__main__":
    menu = MenuAtividades()
    menu.mostrar_menu()
