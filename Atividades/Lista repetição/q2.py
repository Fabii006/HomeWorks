usuario = str(
    input("Informe um número de usuário: ")
)
senha = str(
    input("Informe uma senha: ")
)
while senha==usuario:
    print("ERRO!\n**O usuário não pode ser igual a senha**")
    usuario = str(
    input("Informe um número de usuário: ")
    )
    senha = str(
    input("Informe uma senha: ")
    )

print("Sucesso!")
