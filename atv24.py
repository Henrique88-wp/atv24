# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

soma = 0 
cont = 0
while True:
    numero = int(input("coloque números"))
    if numero == -1:
        break
    soma += numero
    cont += 1
if cont > 0:
    media = soma/cont
    print (f"a média dos números é: {media}")
else:
    print("eu quero números.")