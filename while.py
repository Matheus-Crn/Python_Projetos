#laços de repetição

# num = 1

# while (num <=10): #laço de repetição numerico 
#         print(num)
#         num += 1

nome = None

while True:
    print('Digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'bem-vindo , {nome}')