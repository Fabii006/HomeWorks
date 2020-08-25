n1 = float(
    input("Informe o preço do primeiro produto: ")
)
n2 = float(
    input("Informe o preço do segundo produto: ")
)
n3 = float(
    input("Informe o preço do terceiro produto: ")
)
x=0
if n1<n2 and n1<n3:
    menor = 'primeiro'
elif n2<n1 and n2<n3:
    menor = 'segundo'
elif n3<n1 and n3<n2:
    menor = 'terceiro'
else:
    print('Todos os preços são iguais')
    x=1
if x==0:
    print('Compre o {} produto, pois é o mais barato.'.format(menor))