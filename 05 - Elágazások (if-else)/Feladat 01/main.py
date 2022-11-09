number: int = None

print("Adja meg a vizsgálandó számot > ", end="")
number = int(input())

if number > 0:
    print(f"A szám ({number}) nagyobb, mint nulla!")
elif number < 0:
    print(f"A szám ({number}) kisebb, mint nulla!")
else:
    print(f"A szám ({number}) pontosan nulla!")