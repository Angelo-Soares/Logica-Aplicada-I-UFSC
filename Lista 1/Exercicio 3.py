# 3. Adapte o algoritmo anterior para identificar o maior lado de um triângulo escaleno.
# Estou interpretando que é para adicionar a verificação de se é um traingulo escaleno e mostra qual seu maior lado.

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
        maior = max(lado1, lado2, lado3)
        print("O maior lado do triângulo é:", maior)
else:
    print("Os valores informados não formam um triângulo.")