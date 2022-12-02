currentDay: int = None

currentDay = int(input("Adja meg hányadik napja van a hétnek > "))

match currentDay:
    case 1:
        print("A mai nap: hétfő")
    case 2:
        print("A mai nap: kedd")
    case 3:
        print("A mai nap: szerda")
    case 4:
        print("A mai nap: csütörtök")
    case 5:
        print("A mai nap: péntek")
    case 6:
        print("A mai nap: szombat")
    case 7:
        print("A mai nap: vasárnap")
    case _:
        print("Nincs ilyen nap!")