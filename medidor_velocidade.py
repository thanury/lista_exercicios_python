velocidade = float(input("Digite sua velocidade em km/h: "))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print("Não houve multa.")
elif velocidade <= velocidade_maxima + 10:
    print("Multa leve.")
elif velocidade <= velocidade_maxima + 20:
    print("Multa grave.")
else:
    print("Multa gravíssima.")