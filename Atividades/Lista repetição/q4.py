a = 80000
b = 200000
anos = 0
while a <= b:
    anos +=1
    a = a+(a*0.02)
    b = b+(b*0.015)

print("Foram necessários {} anos".format(anos))