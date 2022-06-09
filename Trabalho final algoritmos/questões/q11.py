# Manuela Fortes
# 188790
def substix2(valores):
    valores2 = []
    for i in(valores):
        if i%2==0:
            valores2.append(i)
        else:
            z = i*2
            valores2.append(z)
    return valores2
x = int(input())
lista = []
for i in range(x):
    j = int(input())
    lista.append(j)
for i in substix2(lista):
    print(i)