numberOne: int = None
numberTwo: int = None

print("Adj meg kettő db számot > ", end="")
numberOne = int(input())
numberTwo = int(input())

if numberOne > numberTwo:
    print(f"Az első megadott szám ({numberOne}) a nagyobb")
elif numberTwo > numberOne:
    print(f"A második megadott szám ({numberTwo}) a nagyobb")
else:
    print("A kettő szám egyenlőek egymással!")