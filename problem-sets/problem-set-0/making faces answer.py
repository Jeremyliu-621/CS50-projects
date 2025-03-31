"""

"
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :(
was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns
that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :(
converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on
that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by
passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
"

Making Faces Answer
Jeremy Liu
2/21/2025

"""

# main function

def main():

    # ask sentence
    sentence = input("Give me your sentence (ADD EMOTICONS): ").strip()
    # plug into convert and print
    print(convert(sentence))

# convert function

def convert(given):
    
    # convert sentence
    return(given.replace(":)", "🙂").replace(":(", "🙁"))

# start main function

main()