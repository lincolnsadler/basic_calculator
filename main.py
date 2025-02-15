num1 = int(input('Digite um número '))
num2 = int(input('Digite outro numero'))
operacao = input('a operação [ + / - / * / ]')

def calculadora (num1, num2, operacao):
    if operacao == '+':
        return(num1 + num2)
    elif operacao == '-':
        return(num1 - num2)
    elif operacao == '*':
        return(num1 * num2)
    elif operacao == '/':
        if num2 == 0:
            print('Error')
        return(num1 / num2)
    else:
        print('operação inválida')

resultado = calculadora(num1, num2, operacao)
print(f'O valor da conta é: {resultado}')

