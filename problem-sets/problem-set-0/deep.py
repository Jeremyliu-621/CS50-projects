"""

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively)
forty-two or forty two. Otherwise output No.

deep.py answers
Jeremy Liu
2/22/2025

"""

# main function

def main():

    # sets the control variable for the loop
    running = True
    while running:

        # prompting users
        response = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").upper().strip()

        # checks if response is appropriate
        if checker(response):
            print("Yes")
        else:
            print("No")
        
        # asks to continue
        if input("Do you want to continue?: ").upper().strip() == "YES":
            running = True
        else:
            print("Bye bye!")
            running = False



# checks response to see if it meets requirements
def checker(response):

    # returns True for the matching cases
    return (response == "42" or response == "FORTY TWO" or response == "FORTY-TWO")

# running main

main()
