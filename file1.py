x = float (input('Введите первое число: '))
y = float (input('Введите второе число: '))

operation = input('Введите оператор: ')

result = None

if operation =='+':
    result = x + y
elif operation =='-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation =='/':
    result = x / y
else:
    print('Неподдерживаемая операция')

print(result)
print(0o43523)