import math
from os import system


a: int = None
b: int = None
muvelet: str = None
eredmeny: float = None

print("Add meg a téglalap szélességét (a) > ", end="")
a = int(input().strip().lower())

print("Add meg a téglalap hosszúságát (b) > ", end="")
b = int(input().strip().lower())
system('echo.')

print("A következő műveletek közül választhat: \nt - terület\nk - kerület\na - átló")
muvelet = str(input().lower().strip())
system('echo.')
system('echo.')

match muvelet:
    case "t":
        eredmeny = a * b
        print(f"A téglalap területe: {eredmeny}")
    case "k":
        eredmeny = 2*(a + b)
        print(f"A téglalap kerülete: {eredmeny}")
    case "a":
        eredmeny = a**2 + b**2
        gyok = math.sqrt(eredmeny)
        print(f"A téglalap átlója: {gyok:1.1f}")
    case _:
        print("Érvénytelen művelet!")