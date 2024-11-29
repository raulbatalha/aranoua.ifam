# Lista de Exercícios 1 – Estruturas de Seleção

Este repositório contém soluções para a **Lista de Exercícios 1** focada em **estruturas de seleção** na programação. Cada exercício propõe um desafio prático envolvendo condições e cálculos. 

## Exercícios

### 1. **Cálculo de Pagamento de Produto**
- Elabore um programa que calcule o valor final de um produto, considerando:
  - O preço normal de etiqueta.
  - A condição de pagamento escolhida.
- As condições são:
  | Código | Condição de Pagamento                                   |
  |--------|--------------------------------------------------------|
  | 1      | À vista em dinheiro ou cheque, recebe 10% de desconto  |
  | 2      | À vista no cartão de crédito, recebe 15% de desconto   |
  | 3      | Em duas vezes, preço normal de etiqueta sem juros      |
  | 4      | Em duas vezes, preço normal de etiqueta com 10% de juros |

---

### 2. **Cálculo do IMC**
- Desenvolva um programa que leia o peso e a altura de um adulto e calcule seu **Índice de Massa Corporal (IMC)**:
  \[
  IMC = \frac{\text{peso}}{\text{altura}^2}
  \]
- Mostre a condição do indivíduo conforme a tabela:
  | IMC       | Condição          |
  |-----------|-------------------|
  | < 18.5    | Abaixo do Peso    |
  | 18.5 - 25 | Peso Normal       |
  | 25 - 30   | Acima do Peso     |
  | > 30      | Obeso             |

---

### 3. **Identificação de Caracteres**
- Crie um algoritmo que identifique se o caractere inserido é:
  - Letra
  - Número
  - Pontuação (`?`, `!`, `.`, `;`, `,`)
  - Caso não se encaixe em nenhum dos itens acima, indique como "Caractere especial".

---

### 4. **Número por Extenso**
- Elabore um programa que leia um número natural entre **0 e 9** e exiba o número por extenso.

---

### 5. **Identificação de Bancos**
- Leia o código de um banco e exiba o nome correspondente:
  | Código | Banco                          |
  |--------|--------------------------------|
  | 1      | Banco do Brasil               |
  | 33     | Santander                     |
  | 104    | Caixa Econômica Federal       |
  | 237    | Bradesco                      |
  | Outro  | Banco não identificado        |

---

### 6. **Cálculo de Idade e Direitos**
- Leia o ano de nascimento de uma pessoa e:
  - Calcule sua idade em relação ao ano corrente (**2023**).
  - Verifique se ela já tem idade para:
    - **Votar** (maior ou igual a 16 anos).
    - **Tirar a Carteira de Habilitação** (maior ou igual a 18 anos).

---

### 7. **Cálculo de Imposto de Renda**
- Com base na **tabela de alíquota do imposto de renda de 2023**, leia o salário de um indivíduo e calcule:
  - A alíquota correspondente.
  - O valor do imposto mensal a ser pago.

  | Base de Cálculo (R$)        | Alíquota (%) |
  |-----------------------------|--------------|
  | Até 1.903,98                | 0,0          |
  | 1.903,99 - 2.826,65         | 7,5          |
  | 2.826,66 - 3.751,05         | 15,0         |
  | 3.751,06 - 4.664,68         | 22,5         |
  | Acima de 4.664,68           | 27,5         |

---

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/raulbatalha/lista-exercicios-aranoua.git
   ```
2. Navegue até o diretório do exercício desejado.
3. Execute o programa com seu ambiente preferido (Python, Java, etc.).

---

## Tecnologias Utilizadas
- **Linguagem**: A escolha da linguagem é livre, mas recomenda-se **Python** pela sua simplicidade e clareza.
- **Ambiente**: Qualquer IDE ou editor de texto (VSCode, PyCharm, etc.).

---

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para:
- Sugerir melhorias.
- Reportar problemas.
- Adicionar novas implementações.

---

## Licença
Este projeto está sob a licença [MIT](LICENSE).