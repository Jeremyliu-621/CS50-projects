"""

In Massachusetts, home to Harvard University, it’s possible to request a vanity license 
plate for your car, with your choice of letters and numbers instead of random ones. 
Among the requirements, though, are:

“All vanity plates must start with at least two letters.”

“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a 
minimum of 2 characters.”

“Numbers cannot be used in the middle of a plate; they must come at the end. For 
example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.

The first number used cannot be a ‘0’.”

“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then 
output Valid if meets all of the requirements or Invalid if it does not. Assume that 
any letters in the user’s input will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements and False if it does not. 

Assume that s will be a str. You’re welcome to implement additional functions for 
is_valid to call (e.g., one function per requirement).

plates.py answers
Jeremy Liu
3/9/2025

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    letters = list(s)
    print(letters)

    if (two_checker(letters) and maxmin_checker(letters) and middle_checker(letters) 
        and zero_checker(letters) and syntax_checker(letters)):
        return True

def two_checker(letters):
    """
    “All vanity plates must start with at least two letters.”
    """
    if int(len(letters)) < 2:
        print("INCORRECT: vanity plates start with at least two letters")
        return False
    elif int(len(letters)) > 1 and (not letters[0].isalpha() or not letters[1].isalpha()):
        print("INCORRECT: vanity plates start with at least two letters")
        return False
    else:
        print("CORRECT  : vanity plates does not start with at least two letters")
        return True

def maxmin_checker(letters):
    """
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a 
    minimum of 2 characters.”
    """
    if int(len(letters)) > 6:
        print("INCORRECT: maximum of 6 characters (letters or numbers) and a minimum of 2 characters")
        return False
    else:
        print("CORRECT  : maximum of 6 characters (letters or numbers) and a minimum of 2 characters")
        return True
    
def middle_checker(letters):
    """
    “Numbers cannot be used in the middle of a plate; they must come at the end. For 
    example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    """
    for i in range(len(letters)-1):
        if letters[i].isnumeric() and letters[i+1].isalpha():
            print("INCORRECT: Numbers used in the middle of a plate")
            return False
        # no else because than un-wrong stuff would print
        # just need all bad letters out, after that, and if no bad letters, return True
    print("CORRECT  : Numbers not used in the middle of a plate; they come at the end")
    return True

def zero_checker(letters):
    """
    The first number used cannot be a ‘0’.”
    """
    for i in range(len(letters)-1):
        if letters[i].isnumeric() and letters[i+1].isnumeric() and int(letters[i]) == 0:
            print("INCORRECT: The first number used is a ‘0’.”")
            return False
    print("CORRECT  : The first number used is not be a ‘0’.”")
    return True

def syntax_checker(letters):
    """
    “No periods, spaces, or punctuation marks are allowed.”
    """
    incorrect_syntax = [
    ".", ",", ";", ":", "!", "?", "-", "_", "(", ")", "[", "]", "{", "}", 
    "'", '"', "`", "…", "—", "–", "/", "\\", "|", "@", "#", "$", "%", "^", 
    "&", "*", "+", "=", "<", ">", "~", " "
]
    for letter in letters:
        if letter in incorrect_syntax:
            print("INCORRECT: periods, spaces, or punctuation marks are used")
            return False
    print("CORRECT  : no periods, spaces, or punctuation marks are used")
    return True

main()