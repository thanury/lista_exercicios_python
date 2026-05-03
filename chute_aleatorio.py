import random

numero_secreto = random.randint(1, 10)
acertou = False
while acertou == False:
    chute = int(input('Insira um número de 1 a 10: '))

    if chute > numero_secreto:
        print('Seu número é MAIOR que o número do sistema.')
    elif chute < numero_secreto:
        print('Seu número é MENOR que o número do sistema.')
    else:
        print('Parabéns! você acertou o número')
        acertou = True