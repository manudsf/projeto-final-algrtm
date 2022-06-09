# Manuela Fortes
# 188790
x = 0
lista = []
soma = 0
while x==0:
    y = float(input())
    if y==0.0:
        x+=1
    else:
        lista.append(y)
for n in lista:
    soma +=n
j = len(lista)
media = soma/j
print(f'Média: {media:.2f}')
print('Maiores que a média:')
for i in lista:
    if i > media:
        print(i)