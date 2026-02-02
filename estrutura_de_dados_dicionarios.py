# MANIPULANDO DICIONARIOS

cliente = {"nome": "leonid",
           "cidade": "são roque",
           "ano_nasc": 1976,
           "ativo": "false"
}
print(cliente["nome"])

cliente["ano_nasc"] = 2000
print(cliente)

del cliente["cidade"]

print(cliente)

if "ano_nasc" in cliente:
    print(f"O cliente nasceu em: {cliente['ano_nasc']}")
else:
    print(f"Não existe a chave ano_nasc")

print(f"lista de valores:")
for valores in cliente.values():
    print(valores)

print(f"lista de chaves:")
for chave, valores in cliente.items():
    print(chave)