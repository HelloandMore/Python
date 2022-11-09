number: int = None

print("Add meg a vizsgálandó számot > ", end="")
number = int(input())

if number < 0:
    print(f"A szám ({number}) kisebb, mint nulla!")
elif number > 0:
    print(f"A szám ({number}) nagyobb, mint nulla!")
else:
    print(f"A szám ({number}) pontosan nulla!")