# Manuela Fortes
# 188790
x = 0
c = ''
while x==0:
    n = input()
    if n ==('FIM'):
        x +=1
    elif len(n) > len(c):
        c = n
        y = len(n)
print(f'A cidade com nome mais extenso é {c}, com {y:.0f} caracteres')