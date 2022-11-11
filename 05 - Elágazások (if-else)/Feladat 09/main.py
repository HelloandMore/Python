from os import system

number1: int = None
number2: int = None

print("Add meg az első (x) számot > ", end="")
number1 = int(input())
system('echo.')

print("Add meg a második (y) számot > ", end="")
number2 = int(input())
system('echo.')

if number1%number2 == 0:
    print(f"Az X ({number1}) OSZTÓJA az Y-nak ({number2})")
elif number2%number1 == 0:
    print(f"Az Y ({number2}) OSZTÓJA a X-nek ({number1})")
else:
    print(f"A két szám NEM OSZTHATÓ egymással ({number1} ; {number2})")