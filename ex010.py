def converte_Dolar(dolar, real):
    conversao = real / dolar
    print(f'Com R$ {real:.2f} você pode comprar U$ {conversao:.2f}')
    return

print('Bem vindo ao programa\n')

print(f'{:=*20}')


real = float(input('Digite quantos Reais deseja converter. R$: '))

resultado = converte_Dolar(dolar, real)

#dolar = float(input('Digite a cotação do Dolar hoje. U$: '))