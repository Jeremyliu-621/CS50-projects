"""

In a file called extensions.py, implement a program that prompts the user for the name of a file
and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
which is a common default.

extension.py answers WITH DICTIONARIES AND SPLITTING
Jeremy Liu
7/10/2025

"""

def main():

    cont = True
    while cont:

        file_conversion = {
            "gif": "image/gif",
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg",
            "png": "image/png",
            "pdf": "application/pdf",
            "txt": "text/plain",
            "zip": "application/zip"
        }

        file_name = input("File name: ").strip()
        name_parts = file_name.rsplit(".")

        if name_parts[1] in file_conversion:
            print(f"!: {file_conversion[name_parts[1]]}")
        else:
            print("application/octet-stream")
        
        cont = input("Continue? (yes/no): ").strip().lower() == "yes"
        
main()