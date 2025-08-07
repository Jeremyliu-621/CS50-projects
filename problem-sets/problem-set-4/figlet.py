"""

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:

Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two 
should be -f or --font, and the second of the two should be the name of the font.

Prompts the user for a str of text.
Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second 
is not the name of a font, the program should exit via sys.exit with an error message.

"""

from pyfiglet import Figlet
import random
import sys

def main():

    figlet = Figlet()
    print(len(sys.argv))

    if len(sys.argv) in [0, 2]:
        
        prompt = input("Input: ")

        if len(sys.argv) == 0:
            figlet.setFont(font=(figlet.getFonts(random(0, len(figlet.getFonts())-1))))
            print(figlet.renderText(prompt))
        else:
            if sys.argv[0] not in ["-f", "--font"] or sys.argv[1] not in figlet.getFonts():
                sys.exit('sys.argv[0] not in ["-f", "--font"] or sys.argv[1] not in figlet.getFonts()')
            else:
                figlet.setFont(font=prompt)
            print(figlet.renderText(prompt))
    else:
        print("not correct!")

main()