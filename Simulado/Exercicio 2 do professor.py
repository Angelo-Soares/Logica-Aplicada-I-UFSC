# Simulado - Questão 2

# Crie um programa que possua uma função chamada classificar_imc que receba dois parâmetros: nome (texto) e imc (float).
#  A função deve retornar uma mensagem conforme as faixas:
# Abaixo de 18.5: "nome está abaixo do peso."
#
# De 18.5 a 24.9: "nome está com peso normal."
#
# De 25.0 a 29.9: "nome está com sobrepeso."
#
# 30.0 ou mais: "nome está obeso."
#
# No programa principal, solicite o nome e o IMC de várias pessoas e mostre a classificação. O programa deve continuar até o usuário informar "sair" como nome.

# Declarations
nome = ""
imc = 0

# Functions

# Função para classificar IMC
def classificar_imc(nome: str, imc: float) -> str:
    min_imc = 18.5
    lim1_imc = 24.9
    max_imc = 30.0

    if imc < min_imc:
        return f"{nome} está abaixo do peso."
    elif min_imc <= imc <= lim1_imc:
        return f"{nome} está com peso normal."
    elif lim1_imc < imc < max_imc:
        return f"{nome} está com sobrepeso."
    else:
        return f"{nome} está obeso."


# Função principal
def main():
    pessoas = []  # lista para armazenar (nome, imc, classificação)

    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            print("\nPrograma encerrado.")
            break

        try:
            imc = float(input("Digite o valor do IMC: "))
            classificacao = classificar_imc(nome, imc)
            print(classificacao)

            # Armazena os dados
            pessoas.append((nome, imc, classificacao))

        except ValueError:
            print("Erro: digite um valor numérico válido para o IMC.")

    # Exibe o ranking em ordem crescente de IMC
    if pessoas:
        print("\n=== Ranking de IMC (crescente) ===")
        pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])
        for pos, (nome, imc, classificacao) in enumerate(pessoas_ordenadas, start=1):
            print(f"{pos}º lugar - {nome}: IMC = {imc:.2f} -> {classificacao}")

        # Calcula e exibe a média dos IMCs
        imcs = [imc for _, imc, _ in pessoas]
        media_imc = sum(imcs) / len(imcs)
        print(f"\nMédia dos IMCs cadastrados: {media_imc:.2f}")


# Execução do programa
if __name__ == "__main__":
    main()