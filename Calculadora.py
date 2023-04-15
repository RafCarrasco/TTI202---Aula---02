#Adição
def adicao(x, y):
    return x + y

#Subtração
def subtracao(x, y):
    return x - y

#Multiplicação
def multiplicacao(x, y):
    return x * y

#Divisão
def divisao(x, y):
    return x / y

print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Digite a opção (1/2/3/4): ")

# Escolher numeros
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executa
# Caso o usuário digite 1, será feito a operação de soma
if operacao == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
# Caso o usuário digite 2, será feito a operação de subtração
elif operacao == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
# Caso o usuário digite 3, será feito a operação de multiplicação
elif operacao == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
# Caso o usuário digite 4, será feito a operação de divisão
elif operacao == '4':
     print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Está operação está inválida")

