'''5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.'''

import string

#Selecionando o texto indicado, retirando os caracteres especiais e separando as palavras
texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
texto = texto.replace('.', ' ').replace(',', ' ').replace(':', ' ')
texto = texto.lower()
texto = texto.split()

#Criando a função para determinar as letras que compõem a palavra "python"
def python(p):
    for c in p:
        if c in 'python':
            return True
        return False

#Calculando quantas palavras do texto possuem uma das letras de "python" e mais de 4 letras
resp = [p for p in texto
if python(p) and len(p)>4]

#Imprimindo o número de palavras que se encaixam nos termos da função
print(resp)
print(len(resp))
