n1 = float(
    input('Informe o primeiro número: ')
)
n2 = float(
    input('Informe o segundo número: ')
)
n3 = float(
    input('Informe o terceiro número: ')
)
x=0
if n1>n2 and n1>n3:
    maior = n1
elif n2>n3 and n2>n1:
    maior = n2
elif n3>n2 and n3>n1:
    maior = n3
else:
    print("Os três números são iguais")
    x = 1
if n1<n2 and n1<n3:
    menor = n1
elif n2<n1 and n2<n3:
    menor = n2
elif n3<n1 and n3<n2:
    menor = n3
if x == 0:
    print('O maior número é {}, e o menor é {}'.format(maior, menor))