numberOne: int = None
numberTwo: int = None

print("Adj meg kettő db számot > ", end="")
numberOne = int(input())
numberTwo = int(input())

if numberOne > numberTwo:
    print(f"{numberTwo} {numberOne}")
elif numberTwo > numberOne:
    print(f"{numberOne} {numberTwo}")
else:
    print(f"A két szám egyenlőek egymással!")