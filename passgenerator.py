import random
import platform, os

sO = platform.system()
if sO == "Linux" or "macOS":
    os.system('clear')
if sO == "Windows":
    os.system('cls')

"""
Describe: password generator simple to my first commit on github
Version: v1.0
Autor: Marcos Prado
"""

print("""                                                                         
 _____                             _    _____                     _           
|  _  |___ ___ ___ _ _ _ ___ ___ _| |  |   __|___ ___ ___ ___ ___| |_ ___ ___ 
|   __| .'|_ -|_ -| | | | . |  _| . |  |  |  | -_|   | -_|  _| .'|  _| . |  _|
|__|  |__,|___|___|_____|___|_| |___|  |_____|___|_|_|___|_| |__,|_| |___|_|  

Version: v1.0
Autor: Marcos Prado                                                                
""")

possCarac = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P','Q','R','S','T','U',
    'V', 'W', 'X', 'Y', 'Z', 'a','b','c','d','e','f',
    'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q',
    'r', 's', 't', 'u', 'v', 'w','x','y','z',' ','!',
    '"', '#', '$', '%', '&', '(',')','*','+','=','-',
    ',', '.', ':', '/', ';', '>','<','?','[',']','{',
    '}', '~', '_', '|'
]

caracSenha = input("[*] How much caracter:  ")
cond = caracSenha.isnumeric()

while cond == False:
    print("Only number...")
    caracSenha = input("[*] How much caracter:  ")
    if caracSenha.isnumeric() == True:
        cond = True

carac = 1
poss = []
listSenhas = ''

while carac <= int(caracSenha):
    poss.append(random.choice(possCarac))
    carac += 1

for i in poss:
    listSenhas += i

print('\n')
print('='*50)    
print(f"Password: {listSenhas}")
print('='*50)

print("Stay safe!")
