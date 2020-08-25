n1 = float(
    input('informe o primeiro número: ')
)
n2 = float(
    input('informe o segundo número: ')
)
n3 = float(
    input('informe o terceiro número: ')
)

if n1>n2 and n1>n3:
    print('maior: ', n1)--
elif n2>n1 and n2>n3:
    print('maior: ', n2)
elif n3>n1 and n3>n2:
    print('maior: ', n3)
