"""

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank 
is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a 
fraction, formatted as X/Y, wherein each of X and Y is an integer, and then 
outputs, as a percentage rounded to the nearest integer, how much fuel is in 
the tank. If, though, 1% or less remains, output E instead to indicate that 
the tank is essentially empty. And if 99% or more remains, output F instead 
to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead 
prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch 
any exceptions like ValueError or ZeroDivisionError.

fuel.py answers
Jeremy Liu
3/17/2025

"""

def main():
    """
    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead 
    prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch 
    any exceptions like ValueError or ZeroDivisionError.
    """
    X, Y = get_nums("Fraction: ")
    calculator(X, Y)

def get_nums(prompt):
    """
    (1)
    prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then 
    outputs, as a percentage rounded to the nearest integer, how much fuel is in 
    the tank.
    (2)
    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead 
    prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch 
    any exceptions like ValueError or ZeroDivisionError.
    """

    while True:
        try:
            X, Y = input(prompt).split("/") # yo idk what this is
            print(f"X is {X}\nY is {Y}")
            X = int(X)
            Y = int(Y)

        except (ValueError, ZeroDivisionError):
            print("pass")
            pass
        else:
            if X > Y or Y == 0:
                print("X > Y or Y == 0")
                continue
            else:
                return X, Y

def calculator(num1, num2):
    """
    (1)
    outputs, as a percentage rounded to the nearest integer, how much fuel is in 
    the tank.
    (2)
    If, though, 1% or less remains, output E instead to indicate that 
    the tank is essentially empty. And if 99% or more remains, output F instead 
    to indicate that the tank is essentially full.
    """
    answer = (int(num1) / int(num2)) * 100
    if answer <= 1:
        print("E")
    elif answer >= 99:
        print("F")
    else:
        print(f"{round(answer)}%")

main()