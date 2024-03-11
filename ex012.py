valor = float(input('Digite o valor do produto R$: '))
valor_com_desconto = valor - (valor * 0.05)

print(f'O produto custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${valor_com_desconto:.2f}')