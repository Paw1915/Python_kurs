import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
x = float(input("Podaj składnik 1: "))
y = float(input("Podaj składnik 2: "))

def addition(x, y):
    logging.debug(f"Dodaję %g i %g", x, y)
    addition_result = x + y
    print(f"Wynik to {addition_result:g}")
    