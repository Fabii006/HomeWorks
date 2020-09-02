
nome = str(
    input("Informe seu nome [+ 3 caracteres]: ")
)
while len(nome) <= 3: 
    nome = str(
    input("Informe seu nome: [+ 3 caracteres]")
    )
idade = int(
    input("Informe a sua idade [maior que zero e menor que 150]: ")
)
while idade<=0 or idade>=150:
    idade = int(
    input("Informe a sua idade [maior que zero e menor que 150]: ")
)
Salário = float(
    input("Informe seu salário [maior que zero]: ")
)
while Salário<=0:
    Salário = float(
    input("Informe seu salário [maior que zero]: ")
)
sexo = str(
    input("Informe seu sexo [f ou m]: ").upper()
)
while (sexo!="M") and (sexo!="F"):
    sexo = str(
    input("Informe seu sexo [f ou m]: ").upper()
)
estado_civil = str(
    input("Informe seu estado civil [s,c,v,d]: ").upper()
)
while estado_civil!="S" and estado_civil!="C" and estado_civil!="V" and estado_civil!="D":
    estado_civil = str(
    input("Informe seu estado civil [s,c,v,d]: ").upper()
)
print("Nome: {}\nIdade: {}\nsalário: R${}\nsexo: {}\nestado civil: {}".format(nome,idade,Salário,sexo,estado_civil))
