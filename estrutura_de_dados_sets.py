# MANIPULANDO CONJUNTOS - SETS

usuarios = {"ana", "maria"}
usuarios.add("felipe")
print (usuarios)



usuario_digitado = input("Digite seu usuário: ")
if usuario_digitado in usuarios:
    print(f"Usuário cadastrado!")
else:
    print(f"Usuário não cadastrado!")
    
novos_usuarios = {"felipe", "pedro", "marcus"}

print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios)
print(f"uniao: {todos_usuarios}")

usuarios_comuns = usuarios.intersection(novos_usuarios)
print (f"interseção: {usuarios_comuns}")

usuarios_diferentes = usuarios.difference(novos_usuarios)
print (f"diferença: {usuarios_diferentes}")