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

plates.py answers two
Jeremy Liu
7/12/2025

"""

def main():
    plate = list(input("Plate: "))
    print(plate)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def maxmincharacters(plate):
    if 2 <= len(plate) <= 6:
        if plate[0].isalpha() and plate[1].isalpha():
            return True
        else:
            print("NOT plate[0].isalpha() and plate[1].isalpha()")
            return False
    else:
        print("2 >= len(plate) or len(plate) >= 6")
        return False

def midnumbers(plate):
    for element in range(len(plate)-1):
        if plate[element].isnumeric() and plate[element+1].isalpha():
            print("plate[element] in numbers and plate[element+1].isalpha()")
            return False
        if plate[element].isalpha() and plate[element+1] == "0":
            print("plate[element].isalpha() and plate[element+1] == '0'")
            return False
    return True

def characterrules(plate):
    for element in plate:
        if not element.isalnum():
            print("not element.isalnum()")
            return False
    return True

def is_valid(s):
    if maxmincharacters(s) and midnumbers(s) and characterrules(s):
        return True
    else:
        return False

main()