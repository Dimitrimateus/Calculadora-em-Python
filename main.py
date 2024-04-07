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
    #Separação entre as operações em que o usuario pode dar mais que dois valores
    match operacao:
        case "Potenciação":
            vezes = 2
            for c in range(1,vezes +1):
                num = float(input(f"Digite o {c}° número: "))
                lista_numeros.append(num)
        case "Radiciação":
            num = float(input("Digite o número: "))
            time.sleep(0.25)
            while num < 0:
                print(" |  O número tem que ser no mínimo 0 |")
                num = float(input("Digite o número: "))
        case "Logaritimação":
                num = float(input("Digite o número: "))
                base = float(input("Qual a base? "))        
                while base == 0:
                    print(" |  A base não pode ser 0  |")
                    time.sleep(0.25)
                    num = float(input("Digite o número: "))
                    base = float(input("Qual a base? ")) 
        case _:
            vezes = int(input(" |  Com quantos números voce deseja fazer esta operação? "))
            for c in range(1,vezes +1):
                num = float(input(f"Digite o {c}° número: "))
                lista_numeros.append(num)
    resultado = 0 
    #Calculos 
    match operacao: 
        case  "Adição":
            for item in lista_numeros:
                resultado += item
        case "Subtração":
            resultado = lista_numeros[0]
            for item in lista_numeros[1:]:
                resultado -= item
        case "Multiplicação":
            resultado = lista_numeros[0]
            for item in lista_numeros[1:]:
                resultado *= item
        case "Divisão":
            resultado = lista_numeros[0]  
            for item in lista_numeros[1:]:  
                resultado /= item
        case "Potenciação":
            resultado = lista_numeros[0]
            for item in lista_numeros[1:]:
                resultado **= item
        case "Radiciação":
            resultado = round(math.sqrt(num),3)
        case "Logaritimação":
            resultado = round(math.log(num, base)) 
    print(f"O resultado é {resultado}")
    time.sleep(0.25)
    continuar = str(input("|  Você quer fazer mais alguma operação? "))
    time.sleep(0.25)
time.sleep(0.5)
print("Calculadora fechada!")
