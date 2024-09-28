"""
#Zmienne
x = int(input("Podaj liczbe\n"))
iloczyn = 3 * x
print(iloczyn)

# Funkcje
#Deklarowanie funkcji liniowej

def f(x):
    return 2*x+1

x_values = [0,1,2,3]

for x in x_values:
    y = f(x)
    print(y)

#Kreslenie funkcji liniowej za pomocą SymPy

from sympy import *
x = symbols('x')
f = 2*x+1
plot(f)

#Kreslenie funkcji kwadratowej
from sympy import *
x = symbols('x')
f = x**2+1
plot(f)

#Deklarowanie funkcji z dwiema zmiennymi niezaleznymi
from sympy import *
from sympy.plotting import plot3d
x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)
"""
#Sumowanie elementow
x = [1,4,6,2]
n = len(x)
suma = sum(10*x[i] for i in range(0,n))
print(suma)