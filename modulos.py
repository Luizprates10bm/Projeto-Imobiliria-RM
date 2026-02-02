import random
import operacoes
from colorama import Fore, init
init(autoreset=True)



def exibir_menu():
    print("1. soma")
    print("2. subtracao")
    print("3. multiplicacao")
    print("4. divisao")
    print("5. numero aleatorio")
    print("0. sair")

def obter_numeros():
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))
    return [a, b]

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")
    if (opcao == "0"):
       print(f"{Fore.BLUE}Saindo do sistema!")
       break
    
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))
    
    if (opcao == "1"):
      a, b = obter_numeros()
      resultado = operacoes.soma(a, b)
      print (f"Resultado: {resultado}")
    elif opcao == "2":
       a, b = obter_numeros()
       resultado = operacoes.subtracao(a, b)
       print (f"Resultado: {resultado}")
    elif opcao == "3":      
        a, b = obter_numeros()
        resultado = operacoes.multiplicacao(a, b)
        print (f"Resultado: {resultado}")
    elif opcao == "4":
        a, b = obter_numeros()
        if b != 0:
            resultado = operacoes.divisao(a, b)
            print (f"Resultado: {resultado}")
        else:
             print("Não é possivel dividir por 0")
    elif opcao == "5":
        a,b = obter_numeros()
        resultado = random.randint(a, b)
        print (f"Resultado: {resultado}")
    else:
         print(f"{Fore.RED}Opção inválida. Tente novamente")