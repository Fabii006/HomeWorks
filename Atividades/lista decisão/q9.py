n1 = float(
    input("Informe o primeiro número: ")
)
n2 = float(
    input("Informe o segundo número: ")
)
n3 = float(
    input("Informe o terceiro número: ")
)
if n1>n2 and n1>n3:
    maior = n1
elif n2>n3:
    meio = n2
    menor = n3
else:
    meio = n3
    menor = n2
if n1<n2 and n2>n3:
    maior = n2
elif n2>n1:
    meio = n2
    menor = n1
else:
    meio = n1
    menor = n2
if n1<n3 and n2<n3:
    maior = n3
elif n2>n1:
    meio = n2
    menor = n1
else:
    meio = n1
    menor = n2
print('Ordem decrescente: {:.2f},{:.2f},{:.2f}'.format(menor, meio, maior))
