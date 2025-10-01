# 1. Crie um programa que leia as notas (0 a 10) de 15 alunos de uma turma.
# a. Armazenar as notas em uma lista.
# b. Calcular e mostrar:
# c. A maior nota.
# d. A menor nota.
# e. A média da turma.
# f. A quantidade de alunos acima da média


listanotas = []
for i in range(15):
    while True:
        nota = float(input("Digite a nota de do aluno de 0 a 10: "))
        if 0 <= nota <= 10:
            listanotas.append(nota)
            break
        else:
            print("Nota inválida.")
print(f" A maior nota é: {max(listanotas)}")
print(f" A menor nota é: {min(listanotas)}")
print(f" A média das notas é: {sum(listanotas)/len(listanotas)}")
print(f" O número de alunos acima da média é: {sum( 1 for n in listanotas if n > sum(listanotas)/len(listanotas))}")