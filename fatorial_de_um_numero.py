numero = int(input('Digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero + 1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
    print(f'O fatorial de {numero} é {fatorial}')
else:
    print(f'Favor informar apenas números inteiros positivos!')