from colorama import Fore, init
init(autoreset=True)

# Lista que guarda os eventos
eventos = []

# Dicionário que guarda os inscritos de cada evento
inscricoes = {}

# Cadastrar novo evento
def cadastrar_evento():
    print(f"\n{Fore.BLUE}=== Cadastrar Evento ===")
    id_evento = int(input("Digite o ID do evento (ex: 1, 2, 3...): "))
    nome = input("Nome do evento: ")
    data = input("Data do evento: ")
    descricao = input("Descrição: ")
    vagas = int(input("Número de vagas: "))

    evento = {
        "id": id_evento,
        "nome": nome,
        "data": data,
        "descricao": descricao,
        "max_vagas": vagas,
        "vagas_restantes": vagas
    }

    eventos.append(evento)
    inscricoes[id_evento] = []

    print(f"{Fore.GREEN}Evento cadastrado com sucesso!")

# Listar eventos
def listar_eventos():
    print(f"\n{Fore.BLUE}=== Eventos Cadastrados ===")
    tem_evento = False

    for evento in eventos:
        tem_evento = True
        print(f"\n{Fore.MAGENTA}ID: {evento['id']}")
        print(f"{Fore.WHITE}Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Descrição: {evento['descricao']}")
        print(f"Vagas restantes: {evento['vagas_restantes']}")

    if not tem_evento:
        print(f"{Fore.YELLOW}Nenhum evento cadastrado.")

# Inscrever em evento
def inscrever_em_evento():
    print(f"\n{Fore.BLUE}=== Inscrever-se ===")
    listar_eventos()
    id_evento = int(input("Digite o ID do evento: "))
    nome = input("Digite seu nome: ")

    for evento in eventos: 
        if evento["id"] == id_evento:
            if nome in inscricoes[id_evento]: 
                print(f"{Fore.YELLOW}Você já está inscrito nesse evento.")
                return

            if evento["vagas_restantes"] > 0:
                inscricoes[id_evento].append(nome)
                evento["vagas_restantes"] -= 1
                print(f"{Fore.GREEN}Inscrição realizada com sucesso!")
            else:
                print(f"{Fore.RED}Não há mais vagas.") 
            return

    print(f"{Fore.RED}Evento não encontrado.")

# Ver inscritos em evento
def visualizar_inscritos():
    print(f"\n{Fore.BLUE}=== Ver Inscritos ===")
    listar_eventos()
    id_evento = int(input("Digite o ID do evento: "))

    if id_evento in inscricoes:
        print(f"\n{Fore.MAGENTA}Inscritos no evento {id_evento}:")
        tem_inscritos = False
        for nome in inscricoes[id_evento]: 
            print(f"{Fore.WHITE}- {nome}")
            tem_inscritos = True
        if not tem_inscritos:
            print(f"{Fore.YELLOW}Ainda não há inscritos.")
    else:
        print(f"{Fore.RED}Evento não encontrado.")

# Atualizar evento
def atualizar_evento():
    print(f"\n{Fore.BLUE}=== Atualizar Evento ===")
    listar_eventos()
    id_evento = int(input("Digite o ID do evento: "))

    for evento in eventos: 
        if evento["id"] == id_evento: 
            nova_data = input("Nova data: ")
            novo_limite = int(input("Novo número de vagas: "))

            # Contar inscritos 
            inscritos = 0
            for nome in inscricoes[id_evento]:
                inscritos += 1

            if novo_limite < inscritos:
                print(f"{Fore.RED}Não é possível reduzir para menos que o número de inscritos.")
                return

            evento["data"] = nova_data
            evento["max_vagas"] = novo_limite
            evento["vagas_restantes"] = novo_limite - inscritos

            print(f"{Fore.GREEN}Evento atualizado com sucesso!")
            return

    print(f"{Fore.RED}Evento não encontrado.")

# Excluir evento
def excluir_evento():
    print(f"\n{Fore.BLUE}=== Excluir Evento ===")
    listar_eventos()
    id_evento = int(input("Digite o ID do evento: "))

    for evento in eventos:
        if evento["id"] == id_evento:
            eventos.remove(evento)
            del inscricoes[id_evento]
            print(f"{Fore.GREEN}Evento excluído com sucesso!")
            return

    print(f"{Fore.RED}Evento não encontrado.")

# Menu principal
def executar_menu():
    while True:
        print(f"\n{Fore.CYAN}=== MENU ===")
        print("1. Cadastrar evento")
        print("2. Atualizar evento")
        print("3. Ver eventos")
        print("4. Inscrever-se")
        print("5. Ver inscritos")
        print("6. Excluir evento")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_evento()
        elif escolha == "2":
            atualizar_evento()
        elif escolha == "3":
            listar_eventos()
        elif escolha == "4":
            inscrever_em_evento()
        elif escolha == "5":
            visualizar_inscritos()
        elif escolha == "6":
            excluir_evento()
        elif escolha == "0":
            print(f"{Fore.MAGENTA}Sistema encerrado.")
            break
        else:
            print(f"{Fore.RED}Opção inválida.")

# Inicia o sistema
executar_menu()
