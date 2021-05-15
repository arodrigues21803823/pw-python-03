
def calcula_linhas(nome_ficheiro):
    file = open(nome_ficheiro,"r")
    count = 0
    content = file.readlines()
    for line in content:
        if line:
          count += 1
    print(count)

def calcula_caracteres(nome_ficheiro):
    file = open(nome_ficheiro, 'r')
    characters = 0
    lines = file.readlines()
    for line in lines:
        characters = characters + len(line) - len(line.split()) 

    print(characters)

def calcula_palavra_comprida(nome_ficheiro):
    file = open(nome_ficheiro, 'r')
    lines = file.readlines()
    longest_word =' '
    for line in lines:
        i = max(line.split(), key=len)
        if len(i) > len(longest_word):
            longest_word = i
    
    print (longest_word)

def calcula_ocorrencia_de_letras(nome_ficheiro):
    words = {}
    file = open(nome_ficheiro, 'r')
    text = file.read()
    for i in text:
        if i == ' ' or i == '\n':
            continue
        elif i in words:
            words[i] += 1
        else:
            words[i] = 1
    print(words)