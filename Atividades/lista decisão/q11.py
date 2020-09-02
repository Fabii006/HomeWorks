salario = float(
    input("Informe seu salário antigo: ")
)
salario_antigo = salario
p_aumento = 0
v_aumento = 0
v_salario = 0
if salario<=280:
    v_salario = salario + (salario*0.2)
    p_aumento = 20
    v_aumento = (salario*0.2)
elif salario>280 and salario<=700:
    v_salario = salario+(salario*0.15)
    p_aumento = 15
    v_aumento = (salario*0.15)
elif salario>700 and salario<=1500:
    v_salario = salario+(salario*0.1)
    p_aumento = 10
    v_aumento = (salario*0.1)
elif salario>1500:
    v_salario = salario+(salario*0.05)
    p_aumento = 5
    v_aumento = (salario*0.05)
print("-Salário antes do reajuste: R${:.2f}\n-Percentual de aumento aplicado: {:.2f}%\n-Valor do aumento: R${:.2f}\n-Salário após aumento: R${:.2f}".format(salario_antigo,p_aumento,v_aumento,v_salario))