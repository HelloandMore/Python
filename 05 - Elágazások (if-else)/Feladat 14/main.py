from os import system

x: int = None
y: int = None
z: int = None

print("Add meg az 'X' értékét > ", end="")
x = int(input())
print("Add meg az 'Y' értékét > ", end="")
y = int(input())
print("Add meg a 'Z' értékét > ", end="")
z = int(input())
print("")

if (x%y == 0):
    print("Az 'X' osztható 'Y'-nal és")
else:
    print("Az 'X' nem osztható 'Y'-nal, és")

if (z%x == 0 and z%y == 0):
    print("a 'Z' oszható 'X'-szel és 'Y'-nal!")
else:
    print("a 'Z' nem osztható 'X'-szel és 'Y'-nal!")