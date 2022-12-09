kezdo: int = None
vegso: int = None
osszeg: int = 0
elsoSzam: int = 0
masodikSzam: int = 0
elso: bool = True

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())
print("Adja meg a végső értéket: ", end='')
vegso = int(input())

if kezdo > vegso:
    for i in range(vegso, kezdo + 1, 1):
        if elso:
            osszeg += i
            elso = False
        else:
            osszeg -= i
            elso = True
    print(osszeg)

elif vegso > kezdo: 
    for i in range(kezdo, vegso + 1, 1):
        if elso:
            osszeg += i
            elso = False
        else:
            osszeg -= i
            elso = True
    print(osszeg)
else:
    print("A két szám egyenlő, vagy érvénytelen!")