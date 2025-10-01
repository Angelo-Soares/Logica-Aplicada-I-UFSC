# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino,
# Sexo Inválido

sexo = input("Digite o sexo (M/F): ")
if sexo == "M":
    print("Masculino")
elif sexo == "F":
    print("Femenino")
else:
    print("Sexo Inválido.")