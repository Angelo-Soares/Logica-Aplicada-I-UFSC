# 3. Crie um programa para analisar salários de funcionários.
# O programa deve ter uma função chamada analisar_salarios que receba uma lista com
# os valores dos salários.
# A função deve retornar:
# a. O total de funcionários.
# b. O maior salário.
# c. O menor salário.
# d. A quantidade de funcionários que ganham acima de R$ 3.000,00.
# e. A média dos salários.
# f. O programa deve:
# g. Ler os salários até o usuário digitar -1.
# h. Chamar a função e exibir os resultados.

def analisar_salarios (salario):
    total_funcionarios = len(salario)
    maior_salario = max(salario)
    menor_salario = min(salario)
    acima_3000 = sum(1 for n in salario if n > 3000)
    media_salario = sum(salario) / len(salario)

    return {
        "total_funcionarios": total_funcionarios,
        "maior_salario": maior_salario,
        "menor_salario": menor_salario,
        "acima_3000": acima_3000,
        "media_salario": media_salario,
    }

def main():
    salarios = []

    print("Digite os salários dos funcionários (ou -1 para sair)")
    while True:
        try:
            salario = float(input("Salario: R$ "))
            if salario == -1:
                break
            elif salario < 0:
                print("Salário inválido.")
            else:
                salarios.append(salario)
        except ValueError:
            print("Digite um salário válido")

    resultado = analisar_salarios(salarios)

    print(f"Total de funcionários: {resultado['total_funcionarios']}")
    print(f"Maior salário: R$ {resultado['maior_salario']:.2f}")
    print(f"Menor salário: R$ {resultado['menor_salario']:.2f}")
    print(f"Funcionários com salário acima de R$ 3.000,00: {resultado['acima_3000']}")
    print(f"Média salarial: R$ {resultado['media_salario']:.2f}")

if __name__ == "__main__":
    main()