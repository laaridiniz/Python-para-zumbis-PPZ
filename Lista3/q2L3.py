usuário = input('Login: ')
senha = input('Senha: ')
while usuário == senha:
    print('Cadastro inválido.')
    usuário = input('Digite novamente o seu login: ')
    senha = input('Digite novamente a sua senha: ')
print('Acesso permitido.')
