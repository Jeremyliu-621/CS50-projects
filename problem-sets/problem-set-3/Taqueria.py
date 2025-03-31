"""

In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d (which is a common 
way of ending one’s input to a program). After each inputted item, display the total cost 
of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal 
places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. 
Assume that every item on the menu will be titlecased.

Taqueria.py answers
Jeremy Liu
3/22/2025

"""

def main():
    order("(Ctrl+Z+Enter to exit) Item: ")

def order(prompt):
    items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}   
    total = 0

    cont = True
    while cont:
        try:

            order = input(prompt).strip().lower().title()

            if order in items:
                total += items[order]
                print(f"Total: ${total:.2f}")
                
        except EOFError:
            cont = False

main()