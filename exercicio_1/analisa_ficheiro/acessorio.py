import json

def pede_nome():
    exist = False
    nome = input("Insira nome do ficheiro (.txt): ")
    while exist == False:
        try:
            f=open(nome,'r')
            exist = True
        except:
            nome = input("Insira nome do ficheiro (.txt): ")

    return str(nome)


def gera_nome(file):
    f=open(file, 'r')
    fileContent = f.readlines()
    f.close

    file_dict={}

    for line in fileContent:
        (key, value) = line.split()
        file_dict[key] = value

    with open(file.split(".")[0] + ".json", 'w') as json_file:
        json.dump(file_dict, json_file, indent=4)

    return file_dict