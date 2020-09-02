peso = float(
    input("Informe o peso do peixe: ")
)
excesso = 0
if peso>50:
    excesso = peso-50
multa = excesso*4
print("O peso em excesso é de {:.2f}kg\nA multa que João deverá pagar é de R${:.2f}".format(excesso,multa))

