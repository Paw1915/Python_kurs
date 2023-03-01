
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

while operation not in[1, 2, 3, 4]:
    print("Niepoprawne działanie!")
    exit(1)

def check_if_number(input):
    try:
        val = float(input)
    except ValueError:
        print("To nie jest liczba!")
        exit(1)

x = input("Podaj składnik 1: ")
check_if_number(x)
y = input("Podaj składnik 2: ")
check_if_number(y)
x = float(x)
y = float(y)
def addition(x, y):
    logging.debug(f"Dodaję %g i %g", x, y)
    addition_result = x + y
    print(f"Wynik to {addition_result:g}")

def subtraction(x, y):
    logging.debug(f"Odejmuję %g od %g", y, x)
    subtraction_result = x - y
    print(f"Wynik to {subtraction_result:g}")

def multiplication(x, y):
    logging.debug(f"Mnożę %g i %g", x, y)
    multiplication_result = x * y
    print(f"Wynik to {multiplication_result:g}")
    
def division(x, y):
    logging.debug(f"Dzielę %g przez %g", x, y)
    division_result = x / y
    print(f"Wynik to {division_result:g}")

if operation == 1:
    addition(x, y)
elif operation == 2:
    subtraction(x, y)
elif operation == 3:
    multiplication(x, y)
elif operation == 4:
    division(x, y)