turno = input("Informe seu turno: \nM-matutino\nV-vespertino\nN-noturno\n").upper()
if turno == 'M':
    print("Bom dia pa quem")
elif turno == 'V':
    print("Boa tarde")
elif turno == 'N':
    print("Boa noite")
else:
    print("Valor inválido")