# Laços de repetição
# Rangue nunca inclui o último número. Por causa do index
# Dentro do range o 1 número diz por qual irá começar, 0 2 até qual index irá, e 3 a forma como vai pular.
#for item in range(2, 11,2):
#    print(item)

# Lista de nomes
nomes = ["Antonio", "Maria", "Pedro", "Ana"]
dados = [1,"Antonio", True, 2.5]
idades = [13,15,18,30,50,75] 
senhas = ["abc", "segura123", "12345", "python123", "oi"]


for nome in nomes:
    print(nome)

for dado in dados:
    print(dado)

for idade in idades:
    if idade >=18:
        print(f'{idade} é MAIOR de idade')
    else:
        print(f'{idade} é MENOR de idade')

for senha in senhas:
    if len(senha) >= 6:
        print(f'A senha {senha} é válida')
    else:
        print(f'A senha {senha} deve possuir no mínimo 6 caracteres')