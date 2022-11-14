import random

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


caracSenha = int(input("[*] Digite a quantidade de caracteres as senhas terão: "))
carac = 1
poss = []
listSenhas = ''

while carac <= caracSenha:
    poss.append(random.choice(possCarac))
    carac += 1

for i in poss:
    listSenhas += i

print('='*50)    
print(f"Senha: {listSenhas}")
print('='*50)

print("Fique seguro!")  