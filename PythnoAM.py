

from math import * # импорт не правильно был написан


print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => ')) # нужно переоброзовать в float если хотим решать примеры
S = a**2
print("Ruudu pindala", round(S,1))d
P=4*a
print("Ruudu ümbermõõt", round(P,1))
di = a * sqrt(2) # не правильно была написан метод "sqrt" из модуля math 
print("Ruudu diagonaal", round(di, 2))
print()
print("Ristküliku karakteristikud") # была не нужная скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # нужно переоброзовать в float если хотим решать примеры2
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # нужно переоброзовать в float если хотим решать примеры
S=b*c
print("Ristküliku pindala", round(S, 1)) # была не закрытая ковычка, нужно закрывать
P=2*(b+c) # не было знака умножения
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di,1)) # не было закрывающей скобки
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) # нужно переоброзовать в float если хотим решать примеры , не правильно были написаны кавычки
d=2*r
print("Ringi läbimõõt", d)
S=pi*r**2 # pi это константа
print("Ringi pindala", round(S,2)) # округления до двух нужно
C=2*pi*r # pi это константа
print("Ringjoone pikkus", round(C,2)) # округления до двух нужно