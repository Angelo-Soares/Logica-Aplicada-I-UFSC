# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
# do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Digite um número inteiro menor que 1000: "))

if 0 <= num < 1000:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10

    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append(f"{centenas} centena")
        else:
            partes.append(f"{centenas} centenas")

    if dezenas > 0:
        if dezenas == 1:
            partes.append(f"{dezenas} dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    if unidades > 0:
        if unidades == 1:
            partes.append(f"{unidades} unidade")
        else:
            partes.append(f"{unidades} unidades")

    if len(partes) == 3:
        resultado = f"{partes[0]}, {partes[1]} e {partes[2]}"
    elif len(partes) == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    elif len(partes) == 1:
        resultado = partes[0]
    else:
        resultado = "0"

    print(f"{num} = {resultado}")

else:
    print("Número inválido. Digite um inteiro entre 0 e 999.")