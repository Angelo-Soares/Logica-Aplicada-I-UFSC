# 1. Criar um algoritmo para ler os lados de um triângulo e identificar se é equilátero.

lado1 = float(input("Digite o tamanho do primeiro lado: "))
lado2 = float(input("Digite o tamanho do segundo lado: "))
lado3 = float(input("Digite o tamanho do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Professor Ricardo que mostrou isso precisa ser verdade para ser um triângulo na aula de Introdução a Algoritmos
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    else:
        print("O triângulo NÃO é equilátero.")
else:
    print("Os valores informados não formam um triângulo.")