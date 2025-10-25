#define punctuation for excluding it 
def no_punct(string):
    punct = '''!()-[]}{;:'"\,<>./?@#$%^&*_~·+—[...]'''
    for char in string:
        if char in punct:
            string = string.replace(char, "")
    return string

#clean punctuation from ms A
try:
    with open ("A-Homily-1-clean.txt", "r") as apunct:
        aclean = apunct.read()
    with open ("A-Homily-1-cleaner.txt", "w+") as acleaner:
        acleaner.write(no_punct(aclean))
except FileNotFoundError:
    print("File not found")

#clean punctuation from ms P
try:
    with open ("P-Homily-1-clean.txt", "r") as ppunct:
        pclean = ppunct.read()
    with open ("P-Homily-1-cleaner.txt", "w+") as pcleaner:
        pcleaner.write(no_punct(pclean))
except FileNotFoundError:
    print("File not found")