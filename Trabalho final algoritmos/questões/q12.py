# Manuela Fortes
# 188790
x = int(input())
lista = []
for j in range(x):
    y = float(input())
    lista.append(y)
menor = min(lista)
if menor==0:
    for i in lista:
        print(i)
else:
    for i in lista:
        div = (i/menor)
        print(f'{div:.1f}')