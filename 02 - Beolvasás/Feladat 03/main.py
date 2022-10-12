from operator import le
from os import system
from turtle import st

band: str = None
songName: str = None
songLenght: int = None

print("Írja ide a kedvenc együttesed nevét > ", end="")
band: str(input())

print("Melyik a kedvenc száma az együttestől? > ", end="")
songName: str(input())

print("És ez hány perc hosszú? (percekben) > ", end="")
songLenght: int(input())

system("cls")

print(f"Az ön kedvenc együttesének {band} a legjobb zeneszáma {songName}, melynek hossza {songLenght} perc")