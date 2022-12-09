kezdo: int = None
vegso: int = None
osszeg: int = 0
osszeg2: int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())
print("Adja meg a végső értéket: ", end='')
vegso = int(input())

if kezdo > vegso:
    for i in range(vegso, kezdo - 1, -1):
        if i%5 == 0:
            osszeg += i
        elif i%7 == 0:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")

elif vegso > kezdo: 
    for i in range(kezdo, vegso - 1, -1):
        if i%5 == 0:
            osszeg += i
        elif i%7 == 0:
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")
else:
    print("A két szám egyenlő, vagy érvénytelen!")