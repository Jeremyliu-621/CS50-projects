"""

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), 
otherwise known as middle-endian order, which is arguably bad design. Dates in that format 
can’t be easily sorted because the date’s year comes last instead of first. Try sorting, 
for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a 
spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 
1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes 
that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, 
formatting years with four digits, months with two digits, and days with two digits, 
“padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno 
Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.

outdated.py answers
Jeremy Liu
3/22/2025 (or 2025/03/22)

"""

def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]   
    
    parts = []

    date_anno_Domini = input("--------------\n"
    "Input a date in anno Domini\n"
    "(month-day-year order, formatted like 9/8/1636 or September 8, 1636\n"
    "--------------\n"
    "Date: ")

    # replace all "/" and ", " with " " so everything can be split upon parts
    parts = date_anno_Domini.replace("/", " ").replace(", ", " ").split(" ")
    print(parts)

    if parts[0] in months:
        month = int(months.index(parts[0])) + 1
        # + 1 because index starts attributing values starting at 0
    else:
        month = int(parts[0])

    print(f"{parts[2]}-{month:02d}-{int(parts[1]):02d}")

main()

