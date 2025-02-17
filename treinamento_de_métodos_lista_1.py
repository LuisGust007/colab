# -*- coding: utf-8 -*-
"""Treinamento de Métodos - Lista 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DpsQ8EKHBYSTHrqcZITnrGwWn94KAnPv

# Exercícios bases

Exercício 1 - Imprima “Hello World”.
"""

print("Hello world")

"""Exercício 2 - Faça um programa para ler, nome, idade e altura. Imprima uma frase que contenha essas informações."""

name = input("Digite o seu nome: ")
age = input("Digite a sua idade: ")
height = input("Digite a sua altura: ")

print(f"Olá! Meu nome é {name}, tenho {age} anos e a minha altura é de {height}m")

"""Exercício 3 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa."""

import math

a = float(input("Digite o valor do primeiro cateto: "))
b = float(input("Digite o valor do segundo cateto: "))

c = (a**2 + b**2)**0.5

print(f"O valor da hipotenusa é {c}")

"""Exercício 4 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente."""

ang = float(input("Digite um ângulo: "))

rad = math.radians(ang)

print(f"O valor do seno é {math.sin(rad)}, do cosseno é {math.cos(rad)} e da tangente é de {math.tan(rad)}")

"""Exercício 5 - Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 a 500.


"""

import math
cont = 0

for i in range(501):

    if i % 3 == 0 and i % 2 == 0: #Para fazer para TODOS OS PARES basta trocar: i % 2 == 0 por i % 2 != 0
      cont = cont + i

print(cont)

"""Exercício 6 - Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

cont = 0
soma = 0

while n > 0:
  n = float(input("Digite algum número: "))
  if n != 999:
    cont = cont + n
    soma = soma + 1
  else:
    break


print(f"Foram digitados {soma} números e a soma entre eles foi {cont}")

"""Exercício 7 - Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI."""

s = int(input("Digite a quantidade de elementos da sequência de Fibonacci que você quer: "))
cont = 0
vet = []

for i in range(1,s):
  if i == 1:
    vet.append(0)
    vet.append(1)
  else:
    vet.append(vet[i-1] + vet[i-2])

print(vet)
print(vet[0])

"""Exercício 8 - Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

∑ (termos)²
"""

import numpy as np
sum = 0
vet = np.zeros(11)

for i in range(1,11):
  print(f"Digite o número do {i}º elemento")
  vet[i] = int(input())
  sum = sum + vet[i]**2

print(f"O seu vetor é {vet}, e a soma dos seus quadrados resulta em {sum}")

"""Exercício 9 - Escreva um programa em Python que permite verificar se uma matriz é uma matriz de permutação. Uma matriz de permutação é uma matriz quadrada cujos elementos são zeros ou uns, tal que em cada linha e em cada coluna exista um, e apenas um, elemento igual a 1."""

import numpy as np

print("Digite o número de linhas e colunas que você quer")
n = int(input())

vet = np.zeros([n,n])

for i in range(n):
  for j in range(n):
    print(f"Digite ou 0 ou 1 para o {j + 1}º elemento da {i + 1}ª linha da matriz")
    vet[i,j] = int(input())
    som_l = np.sum(vet[i,:])
    som_c = np.sum(vet[:,j])

if som_l > 1 or som_c > 1:
  print("Não é uma matriz de permutação")
else:
  print("É uma matriz de permutação")

"""Exercício 10 - Escreva um programa em Python para preencher uma matriz quadrada A de tamanho 4x4. Depois crie uma outra matriz B que seja o resultado da divisão dos elementos de cada linha pelo respectivo elemento da diagonal principal. Ao final, o programa deverá exibir as duas matrizes."""

import numpy as np

A = np.zeros([4,4])



for i in range(4):
  for j in range(4):
    print(f"Digite o elemento da {i + 1}ª linha da {j + 1}ª coluna")
    A[i,j] = float(input())

print(A)

B = np.zeros([4,4])

for m in range(4):
  for n in range(4):
    B[m,n] = A[m,n] / A[m,m]

print(B)

"""# Aprendendo a fazer gráficos"""

import matplotlib.pyplot as plt # Biblioteca para figuras
import numpy as np # Biblioteca matrizes

fig, ax = plt.subplots()

# Salvar as figuras
name = "Escolha o nome para salvar.png"
fig.savefig(name)

# Colocando dados no gráfico
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) # Colocando elementos manualmente
x = np.linspace(0, 200, 142) # (Ponto inicial, Ponto final, Caminho a ser percorrido)
ax.plot(x , np.cos(x), marker = "o", lw = 0.5, ms = 3, color = "red") # Marker coloca ponto, lw ajusta a espessura da linha,
                                                                      # ms é o tamanho da bola e color é cor

# Colocando as configurações do gráfico
ax.set_xlabel("Eixo X - $\int_{0}^{\pi}sen^2(cos(x^3 + 2x^2 + x -1))$", fontsize = 10) # Legendas do gráfico e funciona LaTeX
ax.set_ylabel("Eixo Y", fontsize = 10)


plt.show()

"""# Derivada"""

from sympy import *
from sympy.plotting import *
init_printing(use_unicode=True)
x, y, z = symbols('x y z')
f = exp(x)*cos(x)
der = f.diff(x)

der

"""# Integral"""

from sympy import *
from sympy.plotting import *
init_printing(use_unicode=True)
x, y, z = symbols('x y z')

f = cos(x)
x0 = float(input("Digite o limite inferior: "))
x1 = pi/4

integrate(f,(x,x0,x1))

g = x**2 + 2*x + 3
Integral(g)

"""# Tabela"""

import pandas as pd

col = ['Coluna 1', 'Coluna 2', 'Coluna 3']
lin = ['Linha 1', 'Linha 2', 'Linha 3']
dat = [[1,2,3], [4,5,6],[7,8,9]]

df = pd.DataFrame(dat, index = lin, columns = col)

df