valor = float(
    input("Informe um valor: ")
)
if valor > 0:
    result = 'positivo'
elif valor < 0:
    result = 'negativo'
else:
    result = 'zero'
print("O valor digitado é {}".format(result))