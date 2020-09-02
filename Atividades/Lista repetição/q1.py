nota = float(
    input("Informe uma nota entre 0 e 10: ")
)
while nota<0 or nota>10:
    print("nota inválida!")
    nota = float(
        input("Informe uma nota entre 0 e 10: ")
    )
print("nota :",nota)