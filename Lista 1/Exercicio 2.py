# 2. Adapte o exemplo anterior para identificar um triângulo isósceles (2 lados iguais).
# Estou interpretando que é para adcionar a verificação de traingulo isóceles.

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo não é equilátero nem isósceles.")
else:
    print("Os valores informados não formam um triângulo.")