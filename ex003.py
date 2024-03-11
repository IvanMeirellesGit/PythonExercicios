def soma(n1, n2):
    soma = n1 + n2
    return soma

n1 = int(input('Valor: '))
n2 = int(input('Valor: '))

print('A soma entre {0} e {1} vale: {2}'.format(n1, n2, soma(n1, n2)))