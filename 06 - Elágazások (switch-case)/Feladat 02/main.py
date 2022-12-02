from os import system


monthName: str = None
monthNumber: int = None

monthName = str(input("Adja meg az adott hónapot > ").lower().strip())

system('echo.')

match monthName:
    case "január":
        print("A megadott hónap az év ELSŐ hónapja!")
    case "február":
        print("A megadott hónap az év MÁSODIK hónapja!")
    case "március":
        print("A megadott hónap az év HARMADIK hónapja!")
    case "április":
        print("A megadott hónap az év NEGYEDIK hónapja!")
    case "május":
        print("A megadott hónap az év ÖTÖDIK hónapja!")
    case "június":
        print("A megadott hónap az év HATODIK hónapja!")
    case "júlis":
        print("A megadott hónap az év HETEDIK hónapja!")
    case "augusztus":
        print("A megadott hónap az év NYOLCADIK hónapja!")
    case "szeptember":
        print("A megadott hónap az év KILENCEDIK hónapja!")
    case "október":
        print("A megadott hónap az év TIZEDIK hónapja!")
    case "november":
        print("A megadott hónap az év TIZENEGYEDIK hónapja!")
    case "december":
        print("A megadott hónap az év TIZENKETTEDIK hónapja!")
    case _:
        print(f"A megadott név ({monthName}) nem érvényes!")