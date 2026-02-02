import os
from colorama import init, Fore
from cidades import ler_cidades

init(autoreset=True)
def limpar_tela():
    os.system('cls' if os.system == "nt" else 'clear')

def pausar():
    input(f"{Fore.BLUE}Digite ENTER para continuar...")

def processar_opcao(opcao):
    if opcao == "1":
        cidades =  ler_cidades()
        for cidade in cidades:
          print(f"-> {Fore.GREEN}{cidade}")

def exibir_menu():
    print(F"{Fore.GREEN}==== MENU ====")
    print(F"{Fore.GREEN}1. Listar cidades")
    print(F"{Fore.GREEN}2. Adicionar cidade")
    print(F"{Fore.GREEN}3. Buscar cidade")
    print(F"{Fore.GREEN}4. Atualizar cidade")
    print(F"{Fore.GREEN}5. Excluir cidade")
    print(F"{Fore.GREEN}0. Sair")

def executar_sistema():
    exibir_menu()
    opcao = input("Digite a opção desejada: ")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    executar_sistema()

executar_sistema()
