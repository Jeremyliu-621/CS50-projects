"""

When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
as by omitting vowels, much like Twitter was originally called twttr. In a file 
called twttr.py, implement a program that prompts the user for a str of text and 
then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether 
inputted in uppercase or lowercase.

twttr.py answers
Jeremy Liu
3/9/2025

"""

def main():
    cont = True
    while cont:

        letters = list(asker())
        print(f"your letters are {letters}")

        new_letters = []
        for letter in letters:
            if letter.lower() not in ["a", "e", "i", "o", "u"]:
                new_letters.append(letter)
        
        sentence = ""
        abb = sentence.join(new_letters)
        print(f"Output: {abb}")
        print("==============================")

def asker():
    return input("Input: ")

main()