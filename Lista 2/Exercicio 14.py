# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
# a sua média. A atribuição de conceitos obedece à tabela abaixo:
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua primeira nota: "))
media = (nota1 + nota2) / 2

if 9 <= media <= 10:
    conceito = "A"
elif 7.5 <= media:
    conceito = "B"
elif 6 <= media:
    conceito = "C"
elif 4 <= media:
    conceito = "D"
elif 0 <= media:
    conceito = "E"
else:
    conceito = "Valor Inválido"

if conceito == "A" or conceito == "B" or conceito == "C":
    situacao = "Aprovado"
elif conceito == "D" or conceito == "E":
    situacao = "Reprovado"
else:
    situacao = "Inválido"

print(f"A nota 1 é: {nota1}, a nota 2 é: {nota2}")
print(f"A média é {media}.")
print(f"O conceito do aluno é {conceito}.")
print(f"A situação do aluino é {situacao}")