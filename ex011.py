largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area_Parede = largura * altura
qtd_Tinta = area_Parede / 2

print(f'Sua parede tem a dimensão de {largura}X{altura}\n A área da parede é: {area_Parede:.2f} Mts² \n A quantidade de litros de tinta necessária para pintar a parede é de: {qtd_Tinta:.1f} litros')
