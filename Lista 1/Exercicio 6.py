# 6. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa
# pessoa em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))


resultado = (anos * 365) + (meses * 30) + dias
print("A idade da pessoa em dias é:", resultado)