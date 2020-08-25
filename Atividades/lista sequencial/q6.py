raio_informado = input('informe o raio da circunferência: ')
"""
input estava retornando string, por isso o float

"""
PI = 3.14
area = (PI * float(raio_informado)**2)
print("a área é:", area)
