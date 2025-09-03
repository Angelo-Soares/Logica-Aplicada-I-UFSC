# 7. Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
# a. Seu programa deve verificar se a soma de brancos, nulos e válidos equivalem a 100% do número de eleitores que votaram.

total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

verificacao = votos_brancos + votos_nulos + votos_validos

if verificacao != total_eleitores:
    print("A soma dos votos brancos, nulos e válidos não equivalem a 100% do número de eleitores.")
else:
    brancos_porcentagem = (votos_brancos / total_eleitores) * 100
    nulos_porcentagem = (votos_nulos / total_eleitores) * 100
    validos_porcentagem = (votos_validos / total_eleitores) * 100
    print(f'Percentual de votos brancos é: {brancos_porcentagem:}%')
    print(f'Percentual de votos nulos é: {nulos_porcentagem:}%')
    print(f'Percentual de votos válidos é: {validos_porcentagem:}%')