def adicao(resultado,lista_numeros):
    for item in lista_numeros:
        resultado += item
    return resultado

def subtracao(resultado, lista_numeros):
    resultado = lista_numeros[0]
    for item in lista_numeros[1:]:
            resultado -= item
    return resultado

def multiplicacao(resultado,lista_numeros):
    resultado = lista_numeros[0]
    for item in lista_numeros[1:]:
        esultado *= item
    return resultado

def divisao(resultado,lista_numeros):
    resultado = lista_numeros[0]  
    for item in lista_numeros[1:]:  
        resultado /= item
    return resultado

def potenciacao(resultado,lista_numeros):
    resultado = lista_numeros[0]
    for item in lista_numeros[1:]:
        resultado **= item
    return resultado
