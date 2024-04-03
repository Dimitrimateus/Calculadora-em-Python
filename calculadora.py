import time
import math 

continuar = "S"
while continuar == "S" or continuar == "s" or continuar == "SIM" or continuar == "sim":
    print("-"*50)
    print("         Qual operação você deseja fazer? ")
    print("-"*50)
    #Perguntando a operação
    operacao = str(input(" Adição \n Subtração \n Multiplicação \n Divisão \n Potenciação \n Radiciação \n Logaritimação \n "))
    while operacao != "Adição" and operacao != "Subtração" and operacao != "Multiplicação" and operacao != "Divisão" and operacao != "Potenciação" and operacao != "Radiciação" and operacao != "Logaritimação":
        print("-"*100)
        print("    Essa operação é desconhecida, por favor escreva da forma da mesma forma que foi perguntado. ")
        print("-"*100)
        time.sleep(1.25)
        operacao = str(input(" Adição \n Subtração \n Multiplicação \n Divisão \n Potenciação \n Radiciação \n Logaritimação \n "))
    print("-"*50)
    print(f"        A operação escolhida foi {operacao}")
    print("-"*50)
    time.sleep(1)
    lista_numeros = []
    #Separação entre as operações em que o usuario pode dar mais que dois valores
    if operacao == "Potenciação":
        vezes = 2
        for c in range(1,vezes +1):
            num = int(input(f"Digite o {c}° número: "))
            lista_numeros.append(num)
    else:
        vezes = int(input("Com quantos números voce deseja fazer esta operação? "))
        for c in range(1,vezes +1):
            num = int(input(f"Digite o {c}° número: "))
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
    print(f"O resultado é {resultado}")
    time.sleep(1)
    continuar = str(input("Você quer fazer mais alguma operação?"))
    time.sleep(0.25)
time.sleep(1)
print("Calculadora fechada!")


















