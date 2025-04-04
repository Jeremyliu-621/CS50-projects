"""

"
Even if you haven’t studied physics (recently or ever!), you might have heard that 
E=mc^2, wherein 
 E represents energy (measured in Joules), 
 m represents mass (measured in kilograms), and 
 c represents the speed of light (measured approximately as 300000000 meters per second).
 Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass
as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
"

einstein.py answers
Jeremy Liu
2/21/2025

"""

# main function

def main():

    # print the (inputed mass as a float)(speed of light)^2
    print(float(input("m: ")) * 300000000**2)

# start main function

main()


