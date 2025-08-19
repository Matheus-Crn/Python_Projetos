#Simples, Compostos, Encadeado 
n1 = float(input('digite sua nota 1: '))
n2 = float(input('digite sua nota 2: '))

media = (n1 + n2) / 2

if (media >= 7):  #teste logico simples  (se)
        print ("Resultado: Aprovado")
        print ("Parabéns")
elif (media >= 5): #(ou se)
        print ('Você está de recuperação')
else: #(se não)
        print('Aluno reprovado')

print ('Sua média é {}'.format(media))

# import datetime
# hoje = datetime.date.today()

# print(str(hoje))
# print(repr(hoje))