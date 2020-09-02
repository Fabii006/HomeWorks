a = int(
    input("Informe a populaçao inicial da cidade A: ")
)
b = int(
    input("Informe a populaçao inicial da cidade B: ")
)
taxa_a = float(
    input("Informe a taxa de crescimento da cidade A [em %]:")
)
taxa_b = float(
    input("Informe a taxa de crescimento da cidade B [em %]:")
)
anos = 0
if a>b:
    while b <= a:
        anos +=1
        a = a+(a*((taxa_a)/100))
        b = b+(b*((taxa_b)/100))
else:
    while a <= b:
        anos +=1
        a = a+(a*((taxa_a)/100))
        b = b+(b*((taxa_b)/100))


print("Foram necessários {} anos".format(anos))