from operator import eq
from os import system


szam1: int = None
szam2: int = None
muvelet: int = None
equation: str = None
final: int = None


print("Adj meg két számot, amivel szeretnél számolni")
system('echo.')
szam1 = int(input("Első szám > "))
system('echo.')
szam2 = int(input("Második szám > "))
system('echo.')

print("Válasszon a következő műveletek közül: \n1 Összeadaás\n2 Kivonás\n3 Szorzás\n4 Osztás")
system('echo.')
muvelet = int(input("Add meg a választott művelet számát > "))
system('echo.')

match muvelet:
    case 1:
        final = szam1 + szam2
    case 2:
        final = szam1 - szam2
    case 3:
        final = szam1 * szam2
    case 4:
        final = szam1 / szam2

system('echo.')
print(f"A művelet végeredménye: {final}")