#Manipulando lista de dados

nomes = ["Ana", "Pedro"]

print (f"lista original: {nomes}")


# adicionando 2 nomes com for
for cont in range(1, 4):
   novo_nome = input(f"Digite um nome{cont}: ")
   nomes.append(novo_nome)

print(f"lista adicionando nomes: {nomes}")



# adicionando n quantidades de nomes com while
resp = "s"
while resp == "s":
   
   novo_nome = input(f"Digite um nome: ")
   nomes.append(novo_nome)
   resp = input("Deseja cadastra mais um nome[s/n]: ")

print(f"lista adicionando n nomes: {nomes}")

# listando elementos pela posiçao
print(nomes[0])

# removendo os último elemento da lista
nomes.pop()
print(f"Removendo o último: {nomes} ")

# removendo um elemento qualquer
nomes.remove("Pedro")
print (f"Removendo um elemento: {nomes}")

# verificando a existencia de um elemento
nome_pesquisado = input("digite um nome para pesquisar: ")
if nome_pesquisado in nomes:
   print("nome cadastrado")
else:
     print("Nome não cadastrado")