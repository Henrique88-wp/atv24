# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

lista = []

while True:
    a = int(input("digite um número (caso queira terminar digite -1)"))
    if a == -1:
        break
    lista.append(a)

med = sum (lista) / len(lista)
print(f" a média é de: {med}")