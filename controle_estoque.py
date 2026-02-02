import os
from colorama import init, Fore

# Ativa as cores no terminal
init(autoreset=True)

# Dicionário que armazena os produtos
estoque = {}

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que mostra o menu principal
def menu():
    print(f"{Fore.CYAN}\n==== MENU DE OPÇÕES ====")
    print("1. Adicionar produto")
    print("2. Atualizar produto")
    print("3. Excluir produto")
    print("4. Visualizar estoque")
    print("5. Sair")

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip().lower()
    if nome in estoque:
        print(f"{Fore.YELLOW}Produto já existe no estoque!")
    else:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"{Fore.GREEN}Produto adicionado com sucesso!")

# Função para atualizar os dados de um produto já cadastrado
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ").strip().lower()
    if nome in estoque:
        preco = float(input("Novo preço do produto: "))
        quantidade = int(input("Nova quantidade em estoque: "))
        estoque[nome]['preco'] = preco
        estoque[nome]['quantidade'] = quantidade
        print(f"{Fore.GREEN}Produto atualizado com sucesso!")
    else:
        print(f"{Fore.RED}Produto não encontrado.")

# Função para excluir um produto do estoque
def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ").strip().lower()
    if nome in estoque:
        del estoque[nome]
        print(f"{Fore.GREEN}Produto excluído com sucesso!")
    else:
        print(f"{Fore.RED}Produto não encontrado.")

# Função para mostrar todos os produtos no estoque
def visualizar_estoque():
    if not estoque:
        print(f"{Fore.YELLOW}Estoque vazio.")
    else:
        print(f"{Fore.CYAN}\n==== ESTOQUE ATUAL ====")
        for nome, info in estoque.items():
            print(f"{Fore.WHITE}Produto: {nome.capitalize()} | Preço: R${info['preco']:.2f} | Quantidade: {info['quantidade']}")

# Função principal que roda o sistema com o menu em loop
def executar_sistema():
    while True:
        limpar_tela()
        menu()
        opcao = input(f"{Fore.YELLOW}\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            atualizar_produto()
        elif opcao == '3':
            excluir_produto()
        elif opcao == '4':
            visualizar_estoque()
        elif opcao == '5':
            print(f"{Fore.CYAN}Saindo do sistema. Até logo!")
            break
        else:
            print(f"{Fore.RED}Opção inválida. Tente novamente.")

        input(f"{Fore.MAGENTA}\nPressione Enter para continuar...")

# Chama a função principal para iniciar o sistema
executar_sistema()
