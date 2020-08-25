valorPorHora = float(
    input('informe seu ganho por hora: ')
    )
horas = float(
    input('informe o número de horas trabalhadas por mês: ')
    )

salarioBruto = (valorPorHora * horas)
impostoRenda = salarioBruto * 0.011
inss = salarioBruto * 0.08
Sindicato = salarioBruto * 0.05
descontos = (impostoRenda + inss + Sindicato)
salarioLiquido = salarioBruto - (descontos)

print(
    """
    + Salário Bruto : R${}
    - IR (11%) : R${}
    - INSS (8%) : R${}
    - Sindicato ( 5%) : R${}
    = Salário Liquido : R${}
    * Descontos: R${}

    """.format(salarioBruto, impostoRenda, inss, Sindicato, salarioLiquido, descontos)


)
