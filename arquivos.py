def ler_arquivo(nome_arquivo):
     arquivo = open("cidades.txt", "r")
     conteudo = arquivo.read()
     arquivo.close()
     print(f"lendo o arquivo: {nome_arquivo}")
     print (conteudo)



def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "w")
    arquivo.write(conteudo)
    arquivo.close()


def adicionar_arquivo(nome_arquivo, conteudo):
     arquivo = open(nome_arquivo, "a")
     arquivo.write(conteudo)
     arquivo.close()

def ler_linha_arquivo(nome_arquivo):
    print(f"lendo o arquivo linha a linha: {nome_arquivo}")
    for linha in open(nome_arquivo, "r"):
     print(f"=> {linha.strip().capitalize()}")

ler_arquivo("cidades.txt")
escrever_arquivo("cidades.txt", "Carapicuiba\n")
ler_arquivo("cidades.txt")
adicionar_arquivo("cidades.txt", "sobral\n")
adicionar_arquivo("cidades.txt", "jandira\n")
ler_arquivo("cidades.txt")
ler_linha_arquivo("cidades.txt")