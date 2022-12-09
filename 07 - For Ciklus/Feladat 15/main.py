kezdo: int = None
vegso: int = None
osszeg: int = 0

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
kezdo = int(input())
print("Adja meg a végső értéket: ", end='')
vegso = int(input())

if kezdo > vegso:
    for i in range(vegso, kezdo - 1, -1):
        if i%2:
            if i%3 == 0:
                osszeg += 1

elif vegso > kezdo: 
    for i in range(kezdo, vegso - 1, -1):
        if i%2:
            if i%3 == 0:
                osszeg += 1
else:
    print("A két szám egyenlő, vagy érvénytelen!")