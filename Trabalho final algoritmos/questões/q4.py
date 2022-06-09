# Manuela Fortes
# 188790
t = int(input('Tabuada de: '))
d = int(input('De: '))
a = int(input('Até: '))
for i in range(d, a+1):
    print(f'{t:.0f} x {i:.0f} = {t*i:.0f}')