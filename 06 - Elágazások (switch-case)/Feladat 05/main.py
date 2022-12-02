from os import system


r1: int = None
r2: int =  None
kotes: str = None
eredmeny: float = None

r1 = int(input("Adja meg az ellenállás első eredő értékét > ").lower().strip())
r2 = int(input("Adja meg az ellenállás második eredő értékét > "))
kotes = str(input("Adja meg, hogy sorosan, vagy párhuzamosan vannak bekötve (p/s) > "))
system('echo.')

match kotes:
    case "p":
        eredmeny = (r1 + r2) / (r1 * r2)
        print(f"Az ellenállás: {eredmeny} ")
    case "s":
        eredmeny = r1 + r2
        print(f"Az ellenállás: {eredmeny}")
    case _:
        print(f"Helytelen kötés ({kotes})")