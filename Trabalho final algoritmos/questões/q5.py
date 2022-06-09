# Manuela Fortes
# 188790
def calc(n,n1,x):
    if x ==('+'):
        return n+n1
    if x == ('-'):
        return n-n1
    if x == ('*'):
        return n*n1
    if x == ('/'):
        return n/n1
n = int(input('Digite o primeiro valor: '))
n1 = int(input('Digite o segundo valor: '))
x = input('Qual operação? ')
print(f'O resultado da operação de {x} entre {n:.0f} e {n1:.0f} é {calc(n, n1, x):.0f}.')