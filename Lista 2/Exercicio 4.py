# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra:")

vogais = ["a", "e", "i", "o", "u"]

if len(letra) == 1 and letra.isalpha():
    if letra in vogais:
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Entrada invalida.")