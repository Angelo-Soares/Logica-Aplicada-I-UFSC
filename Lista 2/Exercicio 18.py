# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")

if len(data) == 10 and data[2] == "/" and data[5] == "/":
    try:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])

        if 1 <= mes <= 12:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                max_dias = 31
            elif mes in [4, 6, 9, 11]:
                max_dias = 30
            elif mes == 2:
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    max_dias = 29
                else:
                    max_dias = 28
            if 1 <= dia <= max_dias:
                print(f"A data {data} é válida.")
            else:
                print(f"A data {data} não é válida. Dia inválido.")
        else:
            print(f"A data {data} não é válida. Mês inválido.")
    except ValueError:
        print("Formato inválido. Use apenas números no formato dd/mm/aaaa.")
else:
    print("Formato inválido. Use dd/mm/aaaa.")