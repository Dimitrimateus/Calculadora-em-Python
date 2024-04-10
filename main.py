from modules import *
import time
import math 

continuar = "S"
while continuar == "S" or continuar == "s" or continuar == "SIM" or continuar == "sim":
    print(" | Qual operação você quer fazer?  |")
    #Perguntando a operação
    operacao = str(input(" | Adição         | Subtração      |\n | Multiplicação  | Divisão        |\n | Potenciação    | Radiciação     |\n | Logaritimação  | "))
    while operacao != "Adição" and operacao != "Subtração" and operacao != "Multiplicação" and operacao != "Divisão" and operacao != "Potenciação" and operacao != "Radiciação" and operacao != "Logaritimação":
        print("\n Essa operação é desconhecida, por favor escreva da forma da mesma forma que foi perguntado.")
        time.sleep(1.25)
        operacao = str(input("\n | Adição         | Subtração      |\n | Multiplicação  | Divisão        |\n | Potenciação    | Radiciação     |\n | Logaritimação  | "))
    print(f" |  A operação escolhida foi {operacao}  |")
    time.sleep(1)
    lista_numeros = []
    resultado = 0
    #Separação entre as operações em que o usuario pode dar mais que dois valores
    match operacao:
        case "Adição":
            vezes = int(input(" |  Com quantos números voce deseja fazer esta operação? ")) 
            for c in range(1,vezes +1):
                    num = float(input(f"Digite o {c}° número: "))
                    lista_numeros.append(num)
            resultado = print(f"O resultado é {adicao(resultado, lista_numeros)}")
        case "Subtração":
            vezes = int(input(" |  Com quantos números voce deseja fazer esta operação? "))
            for c in range(1,vezes +1):
                    num = float(input(f"Digite o {c}° número: "))
                    lista_numeros.append(num)
            resultado = print(f"O resultado é {subtracao(resultado, lista_numeros)}")
        case "Multiplicação":
            vezes = int(input(" |  Com quantos números voce deseja fazer esta operação? "))
            for c in range(1,vezes +1):
                    num = float(input(f"Digite o {c}° número: "))
                    lista_numeros.append(num)
            resultado = print(f"O resultado é {multiplicacao(resultado,lista_numeros)}")
        case "Divisão":
            vezes = int(input(" |  Com quantos números voce deseja fazer esta operação? "))
            for c in range(1,vezes +1):
                    num = float(input(f"Digite o {c}° número: "))
                    lista_numeros.append(num)
            resultado = print(f"O resultado é {divisao(resultado, lista_numeros)}")
        case "Potenciação":
            vezes = 2
            for c in range(1,vezes +1):
                num = float(input(f"Digite o {c}° número: "))
                lista_numeros.append(num)
            resultado = print(f"O resulatdo é {potenciacao(resultado, lista_numeros)}")
        case "Radiciação":
            num = float(input("Digite o número: "))
            time.sleep(0.25)
            while num < 0:
                print(" |  O número tem que ser no mínimo 0 |")
                num = float(input("Digite o número: "))
            resultado = print(f"O resultado é {round(math.sqrt(num),3)}")
        case "Logaritimação":
                num = float(input("Digite o número: "))
                base = float(input("Qual a base? "))     
                while base == 0:
                    print(" |  A base não pode ser 0  |")
                    time.sleep(0.25)
                    num = float(input("Digite o número: "))
                    base = float(input("Qual a base? ")) 
                resultado = print(f"O reusltado é {round(math.log(num, base)) }")
    time.sleep(0.25)
    continuar = str(input("|  Você quer fazer mais alguma operação? "))
    time.sleep(0.25)
time.sleep(0.5)
print("Calculadora fechada!")
