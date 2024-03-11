print('Programa de aluguel de carros')

dias = int(input('Quantos dias ficou com o carro: '))
km = float(input('Quantos KM foram percorridos: '))
valor_total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R$:{valor_total:.2f}')