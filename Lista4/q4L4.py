'''4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.'''

#Gerando a lista de palavras do texto, após retirar os caracteres especiais e colocar todas as letras em minúsculas
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
texto = texto.replace('.', ' ').replace(',', ' ').replace(':', ' ')
texto = texto.lower()
texto = texto.split()

#Criando a lista com as palavras que começam ou terminam com uma das letras de "python"
resp = []
for p in texto:
    if p[0] in 'python' or p[-1] in 'python':
        resp.append(p)

#Imprimindo a lista
print(resp)