from os import system


selection: int = None

print("Válasszon egy üdítőt: \n1. Coca Cola\n2. Pepsi\n3. Fanta\n4. Sprite")
system('echo.')
selection = int(input("Írja ide az ön választását > "))

match selection:
    case 1:
        print("A választásod a Coca Colára esett")
    case 2:
        print("A választásod a Pepsire esett")
    case 3:
        print("A választásod a Fantára esett")
    case 4:
        print("A választásod a Spritera esett")
    case _:
        print("A választásod ÉRVÉNYTELEN!")