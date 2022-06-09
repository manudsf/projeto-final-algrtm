# Manuela Fortes
# 188790
pares = []
impares = []
for i in range(8):
    x = int(input())
    if x%2==0:
        pares.append(x)
    else:
        impares.append(x)
tp = len(pares)
ti = len(impares)
print(f'{tp:.0f} pares: ')
for par in pares:
    print(par)
print(' ')
print(f'{ti:.0f} impares: ')
for imp in impares:
    print(imp)