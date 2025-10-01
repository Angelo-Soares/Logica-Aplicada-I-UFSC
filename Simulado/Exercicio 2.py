# 2. Crie um programa que possua uma função chamada classificar_imc que receba
# dois parâmetros: nome (texto) e imc (float).
# A função deve retornar uma mensagem conforme as faixas:
# a. Abaixo de 18.5: "nome está abaixo do peso."
# b. De 18.5 a 24.9: "nome está com peso normal."
# c. De 25.0 a 29.9: "nome está com sobrepeso."0,
# d. 30.0 ou mais: "nome está obeso."
# e. No programa principal, solicite o nome e o IMC de várias pessoas e mostre a
# classificação. O programa deve continuar até o usuário informar "sair" como
# nome.

def classificar_imc(nome: str, imc: float) -> str:
    if imc < 18.5:
        return f"{nome} está abaixo do peso."
    elif 18.5 <= imc <= 24.9:
        return f"{nome} está com peso normal."
    elif 25.0 <= imc <= 29.9:
        return f"{nome} está com sobrepeso."
    else:  # 30.0 ou mais
        return f"{nome} está obeso."


def main():
    pessoas = []  # Lista para armazenar (nome, imc, classificação)

    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            print("Programa encerrado.")
            break

        try:
            imc = float(input("Digite o IMC valor do IMC: "))
            classificacao = classificar_imc(nome, imc)
            print(classificacao)
            pessoas.append((nome, imc, classificacao))
        except ValueError:
            print("Digite um número válido para o IMC.")

    # Exibir ranking
    if pessoas:
        print("=== Ranking do maior para o menor IMC ===")
        pessoas.sort(key=lambda x: x[1], reverse=True)  # Ordena pelo IMC (maior -> menor)
        for i, (nome, imc, classificacao) in enumerate(pessoas, start=1):
            print(f"{i}. {nome} - IMC: {imc:.2f} - {classificacao}")
        imcs = [imc for _, imc, _ in pessoas]
        media_imc = sum(imcs) / len(imcs)
        print(f"Média dos IMCs cadastrados: {media_imc:.2f}")
    else:
        print("Nenhum dado foi inserido.")


if __name__ == "__main__":
    main()