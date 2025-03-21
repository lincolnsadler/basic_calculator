num1 = int(input('Digite um número '))
num2 = int(input('Digite outro numero'))
operation = input('a operação [ + / - / * / ]')

def calculator (num1, num2, operation):
    if operation == '+':
        return(num1 + num2)
    elif operation == '-':
        return(num1 - num2)
    elif operation == '*':
        return(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('Error')
        return(num1 / num2)
    else:
        print('Invalid operation')

result = calculator(num1, num2, operation)
print(f'The value is: {result}')

