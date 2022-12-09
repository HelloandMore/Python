kezdo: int = 0
vegso: int = 0
osszeg1: int = 0
osszeg2: int = 0
mennyiseg1: int = 1
mennyiseg2: int = 1
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())
print("Adja meg a végső értéket: ", end='')
vegso = int(input())

if kezdo > vegso:
    for i in range(kezdo, vegso - 1, -1):
        if i%2== 0:
            osszeg1 += i
            mennyiseg1 += 1
        if i%2:
            osszeg2 += i
            mennyiseg2 += 1
    print(f"Páros zsámok átlaga: {osszeg1/mennyiseg1}")
    print(f"Páratlan számok összege: {osszeg2/mennyiseg2}")

elif vegso > kezdo: 
    for i in range(vegso, kezdo - 1, -1):
        if i%2 == 0:
            osszeg1 += i
            mennyiseg1 += 1
        if i%2:
            osszeg2 += i
            mennyiseg2 += 1
    print(f"Páros zsámok átlaga: {osszeg1/mennyiseg1}")
    print(f"Páratlan számok összege: {osszeg2/mennyiseg2}")
else:
    print("A két szám egyenlő, vagy érvénytelen!")