# Manuela Fortes
# 188790
lista = []
for i in range(10):
    x = float(input())
    lista.append(x)
y = 0
lista.reverse()
for i in (lista):
    if i < 0:
        y+=1
        print(i)
        
if y==0:
    print('Nenhum valor negativo')
        
    