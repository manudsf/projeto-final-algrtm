# Manuela Fortes
# 188790
vi = int(input('Valor do imóvel: '))
sl = int(input('Salário: '))
ap = int(input('Anos a pagar: '))
meses = ap*12
pm = vi/meses
tr = sl*0.3
if pm > tr:
    print('Infelizmente você não pode obter o empréstimo')
if pm < tr:
    print('Empréstimo aprovado.')
    print(f'Valor da prestação: {pm:.2f}')