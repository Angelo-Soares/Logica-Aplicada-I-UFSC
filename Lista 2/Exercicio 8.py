# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: "))
listaprod = [prod1, prod2, prod3]

print(f"O produto que você deve comprar é o produto que custa: R$ {min(listaprod)}")