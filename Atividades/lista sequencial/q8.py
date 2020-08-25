ganho = float(
    input("Informe quanto você ganha por hora: ")
)
horas = float(
    input("Informe seu número de horas trabalhadas no mês: ")
)
print("Seu salário é de: R${:.2f}".format(ganho*horas))