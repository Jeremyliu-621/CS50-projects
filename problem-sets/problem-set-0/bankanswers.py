"""

In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

bank.py answers
Jeremy Liu
2/22/2025

"""

# defining the main function
def main():
    '''
    function:   sets the main loop
    parameters: n/a
    return:     n/a
    '''
    total = 0       # total is the 'wallet', each 'wrong' iteration will add values into total.

    cont = True     # main loop. Continues until something returns 'False.' just for fun
    while cont:
        
        # user input -> passing the input and initially-definied total into checker():
        greeting = input("What is your greeting? ").strip().upper()
        total += checker(greeting, total)
        # after EVERYTHING (including functions) are done, the whole iteration can proceed and be repeated
        if input("?: ").upper().strip() == "YES" or "YEAH" or "SURE" or "UH HUH":
            cont = True
        else:
            print("bye bye!")
            cont = False

def checker(greeting, total):
    '''
    function:   determines which greeting case is inputed
    parameters: greeting, total
    return:     changed total from totalwriter(), it's a message carrier essentially
    '''
    if greeting.startswith("H") and greeting != "HELLO":    # not much to explain here, just passes the total and an
        totalwriter(total, 20)                              # amount into another totalwriter():, which writes stuff
    elif greeting == "HELLO":
        totalwriter(total, 0)
    else:
        totalwriter(total, 100)
    return total

def totalwriter(total, amount):
    '''
    function:   uses the determined greeting case to attribute an amount owed to the total amount variable
    parameters: total, amouunt
    return:     changed total
    '''
    print("total before: {total:.2f}")
    total += amount                                         # total = total + amount
    print(f"+{amount:.2f}\ntotal after:  {total:.2f}")
    # return the new total
    return total

# main loop
main()

