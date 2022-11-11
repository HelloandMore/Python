from os import system

number1: int = None
number2: int = None
number3: int = None

print("Adj meg három db számot > ", end="")
number1 = int(input())
system('echo.')
number2 = int(input())
system('echo.')
number3 = int(input())
system('echo.')
system('echo.')

if number1 > number2:
    if number1 > number3:
        if number2 > number3:
            print(number1, number2, number3)
        else:
            print(number1, number3, number2)
    else:
        print(number3, number1, number2)
else:
    if number2 > number3:
        if number3 > number1:
            print(number2, number3, number1)
        else:
            print(number2, number1, number3)
    else:
        print(number3, number2, number1)