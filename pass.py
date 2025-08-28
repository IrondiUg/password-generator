import random, os

logo = ("""\033[1;36m

8888888b.  8888888b.  8888888888 Y88b   d88P 
888  "Y88b 888   Y88b 888         Y88b d88P  
888    888 888    888 888          Y88o88P   
888    888 888   d88P 8888888       Y888P    
888    888 8888888P"  888           d888b    
888    888 888 T88b   888          d88888b   
888  .d88P 888  T88b  888         d88P Y88b  
8888888P"  888   T88b 8888888888 d88P   Y88b            

          \n    ╔═════════════════════════════╗\n    ║  TOOL NAME: {  ULTRON  }    ║\n    ║  AUTHOR   : CHIDEXZY        ║\n    ╚═════════════════════════════╝
          \n""" )

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
num = "1234567890"
spc = "!@#$%&*?"
blends = ["st", "tr", "br", "cr", "dr", "gr", "pr", "pl", "cl", "fr", "bl", "ch", "sh", "th"]
doubles = ["oo", "ee", "ai", "ea", "ou", "ie"]
syllable_patterns = ["CV", "CVC", "CCV", "CVV"]

def make_syllable(pattern):
    syll = ""
    for p in pattern:
        if p == "C":
            if len(syll) == 0 and random.random() < 0.25:
                syll += random.choice(blends)
            else:
                syll += random.choice(consonants)
        elif p == "V":
            if random.random() < 0.2:
                syll += random.choice(doubles)
            else:
                syll += random.choice(vowels)
    return syll

def make_readable_base(length=8):
    word = ""
    while len(word) < length:
        pattern = random.choice(syllable_patterns)
        word += make_syllable(pattern)
    return word[:length]

class Main:
    def __init__(self):
        os.system('clear')
        print(logo)
        print("\033[92;1m [1] ALPHABETS ONLY")
        print("\033[96;1m [2] NUMBERS ONLY")
        print("\033[93;1m [3] ALPHA-NUMERIC")
        print("\033[93;1m [4] ALPHA-NUMERIC + SP")
        print("\033[90;1m [0] EXIT \n")
        select = input("\033[34;1m Choose : \033[92;1m")
        if select in ["1", "01"]:
            alpha()
        if select in ["2", "02"]:
            numb()
        if select in ["3", "03"]:
            an()
        if select in ["4", "04"]:
            ansp()

def alpha():
    password = make_readable_base(10)
    print(f"\n{password}")
    input("")
    Main()

def numb():
    password = ''
    for i in range(1, 11):
        password += random.choice(num)
    print(f"\n{password}")
    input("")
    Main()

def an():
    base = make_readable_base(8)
    password = random.choice(num) + base + random.choice(num)
    print(f"\n{password}")
    input("")
    Main()

def ansp():
    base = make_readable_base(7)
    password = base + random.choice(num) +random.choice(num) + random.choice(spc)
    print(f"\n{password}")
    input("")
    Main()

Main()
