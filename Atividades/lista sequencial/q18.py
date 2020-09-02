tamanho = float(
    input("Informe o tamanho do seu arquivo em [mb]")
)
velocidade = float(
    input("Informe a velocidade do link de internet em [mbps]")
)
tempo = tamanho/(velocidade*60)
print("A velocidade de downloads é de: {:.2f} minutos".format(tempo))
