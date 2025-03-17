import random, time, os, sys

logo = ("""\033[1;36m

8888888b.  8888888b.  8888888888 Y88b   d88P 
888  "Y88b 888   Y88b 888         Y88b d88P  
888    888 888    888 888          Y88o88P   
888    888 888   d88P 8888888       Y888P    
888    888 8888888P"  888           d888b    
888    888 888 T88b   888          d88888b   
888  .d88P 888  T88b  888         d88P Y88b  
8888888P"  888   T88b 8888888888 d88P   Y88b            
          \n%s    ╔═════════════════════════════╗\n%s    ║  TOOL NAME: {  ULTRON  }    ║\n%s    ║  AUTHOR   : CHIDEXZY        ║\n%s    ╚═════════════════════════════╝
          \n""" )

alph = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
spc = '!@#$%&*?'

class Main:
    def __init__(self):
        os.system('clear')
        print(logo)
        print("\033[92;1m [1] ALPHABETS ONLY")
        print("\033[96;1m [2] NUMBERS ONLY")
        print("\033[93;1m [3] ALPHA-NUMERIC")
        print("\033[93;1m [4] ALPHA-NUMERIC + SP")
        print("\033[90;1m [0] EXIT \n")
        select =input("\033[34;1m Choose : \033[92;1m")
        if select in ["1", "01"]:
            alpha()
        if select in ["2", "02"]:
            numb()
        if select in ["3", "03"]:
            an()
        if select in ["4", "04"]:
            ansp()

def alpha():
    password = ''
    for i in range(1, 10):
        password +=random.choice(alph)
    print("Your Password is: " +password)
    input("")
    Main()

def numb():
    password = ''
    for i in range(1, 11):
        password += random.choice(num)
    print("Your Password is: " + password)
    input("")
    Main()

def an():
    password = ''
    for i in range(1, 11):
        password += random.choice(num+alph)
    print("Your Password is: " + password)
    input("")
    Main()

def ansp():
    password = ''
    for i in range(1, 11):
        password += random.choice(num+alph+spc)
    print("Your Password is: " + password)
    input("")
    Main()


Main()
