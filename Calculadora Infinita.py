#1: SOMA
#2: SUBTRAÇÃO
#3: MULTIPLICAÇÃO
#4: DIVISAO
#0: SAIR

def calculadora (num1, num2, operador):
    if (operador == 1):
        return num1 + num2
    elif (operador == 2):
        return num1 - num2
    elif (operador == 3):
        return num1 * num2
    elif (operador == 4):
        return num1 / num2
    else:
        return 0
        
executar = True

while (executar == True):
    print ("Qual operação quer realizar?")
    print ("1:SOMA 2:SUBTRAÇÃO 3:MULTIPLICAÇÃO 4:DIVISÃO 0:SAIR")
    operador = int (input())
    if (operador < 0) or (operador > 4):
        print ("Não Existente")
    elif (operador == 0):
        executar = False
    else:
        print ("Insira o primeiro número para a operação")
        num1 = int(input())
        print ("Insira o segundo número para a operação")
        num2 = int(input())
        resultado = calculadora (num1, num2, operador)
        print ("O resultado é:", resultado)
