"""

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression
and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y
and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

interpreter.py answers
Jeremy Liu
2/23/2025

"""

def main():
    value = 0
    cont = True
    while cont:
        
        all = input("x is an integer\ny is +, -, *, or /\nz is an integer\ngive me your 'x y z' in that format: ")
        x, y, z = all.split(" ")
        x = float(x)
        z = float(z)
        if y == "+":
            value = (x+z)
        elif y == "-":
            value = (x-z)
        elif y == "*":
            value = (x*z)
        elif y == "/":
            value = (x/z)

        float(value)
        print(f"{value:,.1f}")

        if input("? ").lower() != "yes":
            print("bye!!!")
            cont = False

main()