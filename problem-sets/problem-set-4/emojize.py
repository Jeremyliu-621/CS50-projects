"""

Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” 
whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs 
additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be 
automatically converted to 👍.

In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the 
“emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

fuel.py answers
Jeremy Liu
3/17/2025

"""

import emoji

def main():
    languages = ['en', 'es', 'pt', 'it', 'fr', 'de', 'fa', 'id', 'zh', 'ja', 'ko', 'ru', 'ar', 'tr']
    while True:
        lang = input("Language: ").strip().lower()
        if lang in languages:
            break
        else:
            continue
    prompt = input("Input: ")
    print(emoji.emojize((f"Python is {prompt}"), language=lang))

main()
