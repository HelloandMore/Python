kezdo: int = None
vegso: int = None
osszeg: int = 0
mennyiseg: int = 1

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())
print("Adja meg a végső értéket: ", end='')
vegso = int(input())

if kezdo > vegso:
    for i in range(kezdo, vegso - 1, -1):
        osszeg += i
        mennyiseg += 1
    print(osszeg / mennyiseg)
    
elif vegso > kezdo: 
    for i in range(vegso, kezdo - 1, -1):
        osszeg += i
        mennyiseg += 1
    print(osszeg / mennyiseg)
else:
    print("A két szám egyenlő, vagy érvénytelen!")