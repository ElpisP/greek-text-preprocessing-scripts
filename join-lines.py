#filenames
astring = "A-Homily-1-cleaner.txt"
pstring = "P-Homily-1-cleaner.txt"

#join multiple lines to one string in Homily A
try:
    with open (astring, "r") as alines:
        aline = "".join(line.strip() for line in alines)
    with open ("A-Homily-1-joined.txt", "w+") as ajoined:
        ajoined.write(aline)
except FileNotFoundError:
    print("error")

#join multiple lines to one string in Homily P
try:
    with open(pstring, "r") as plines:
        pline = "".join(line.strip() for line in plines)
    with open("P-Homily-1-joined.txt", "w+") as pjoined:
        pjoined.write(pline)
except FileNotFoundError:
    print("error")