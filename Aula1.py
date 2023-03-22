print("Digite a velocidade em m/s:")
velocidade = float(input())
print("Velocidade:", velocidade*3.6)

print(" ")
print("===============================")
print(" ")

import math

print("Digite o radio da circunferência:")
circunferencia = float(input())
print("Velocidade:", circunferencia*2*math.pi)

print(" ")
print("===============================")
print(" ")

print("Digite o número:")
num = float(input())
num0 = num -1 
num1 = num + 1
print('''Anterior: {}
Sucessor: {}'''.format(num0, num1))

print(" ")
print("===============================")
print(" ")

import datetime

print("Digite o seu ano de nascimento:")
nasc = int(input())
ano = datetime.datetime.now().year
if nasc <= 99:
    print("Idade:", ano - 1900 - nasc)
else:
    print("Idade:", ano - nasc)