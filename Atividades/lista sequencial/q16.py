area = float(
    input("Informe a área a ser pintada: ")
)
litros = area/3
latas = litros/18
latas = int(latas+1)
valor = latas *80
print("Você precisará de {} latas de tinta\nValor total: R${:.2f}".format(latas,valor))