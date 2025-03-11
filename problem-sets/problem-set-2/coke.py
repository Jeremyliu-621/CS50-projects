"""

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts 
coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due. Once the user has 
inputted at least 50 cents, output how many cents in change the user is owed. Assume 
that the user will only input integers, and ignore any integer that isn’t an accepted 
denomination.

coke.py answers
Jeremy Liu
3/8/2025

"""

import time

def main():
    coke = 50
    while coke > 0:
        coin = get_coin(coke)
        coke -= coin
    print(f"Change Owed: ${abs(coke)}")
    

def get_coin(due):
    while True:
        print(f"Amount due: ${due}")
        coin = int(input(f"Insert coin: "))
        if coin in [5, 10, 25]:
            return coin
        else:
            time.sleep(0.5)
            print("coin not in [5, 10, 25]")
            time.sleep(0.5)
        
        
main()
