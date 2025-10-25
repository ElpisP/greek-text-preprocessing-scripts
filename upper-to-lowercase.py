#convert upper to lowercase A Homily
try:
    with open ("A-Homily-1-cleaner.txt", "r") as acleanup:
        alower = acleanup.read().lower()
    with open ("A-Homily-1-lowercase.txt", "w+") as acleanlow:
        acleanlow.write(alower)
except FileNotFoundError:
    print("You did wrong")

#convert upper to lowercase P Homily
try:
    with open ("P-Homily-1-cleaner.txt", "r") as pcleanup:
        plower = pcleanup.read().lower()
    with open ("P-Homily-1-lowercase.txt", "w+") as pcleanlow:
        pcleanlow.write(plower)
except FileNotFoundError:
    print("you did wrong")