"""
  Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

"""

tipo = input("Informe qual carne irá comprar: \n 1-Filé Duplo\n 2-Alcatra\n 3-Picanha\n ")
quantidade = float(
    input("Informe a quantidade de carne que irá comprar: ")
)
pagamento = input("Informe o método de pagamento: \n 1-cartão\n 2-dinheiro\n ")
if tipo == '1':
    tipo = 'Filé duplo'
    if quantidade <= 5:
        valor = 4.90 * quantidade
    elif quantidade > 5:
        valor = 5.80 * quantidade
if tipo == '2':
    tipo = 'Alcatra'
    if quantidade <= 5:
        valor = 5.90 * quantidade
    elif quantidade > 5:
        valor = 6.80 * quantidade
if tipo == '3':
    tipo = 'Picanha'
    if quantidade <= 5:
        valor = 6.90 * quantidade
    elif quantidade > 5:
        valor = 7.80 * quantidade
preco = valor
desconto = 0
if pagamento == '1':
    desconto = (valor*0.05)
    valor = valor - (valor*0.05)
    pagamento = 'cartao'
print('---------------CUPOM FISCAL-----------------\nCarne: {}\nQuantidade: {}kg\nPreço total: R${:.2f}\nTipo de pagamento: {}\nDesconto: R${:.2f}\nValor a pagar: R${} '.format(tipo,quantidade,preco,pagamento,desconto,valor))





