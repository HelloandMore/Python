kezdo: int = None
vegso: int = None
osszeg: int = 0
osszeg2: int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input().strip())
print("Adja meg a végső értéket: ", end='')
vegso = int(input().strip())

if kezdo > vegso:
    for i in range(vegso, kezdo - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"A páros számok {osszeg} összege a nagyobb")
    else:
        print(f"A páratlan számok {osszeg2} összege a nagyobb")

elif vegso > kezdo: 
    for i in range(kezdo, vegso - 1, -1):
        if i%2 == 0:
            osszeg += i
        elif i%2:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"A páros számok {osszeg} összege a nagyobb")
    else:
        print(f"A páratlan számok {osszeg2} összege a nagyobb")
else:
    print("A két szám egyenlő, vagy érvénytelen!")