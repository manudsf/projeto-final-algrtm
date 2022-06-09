# Manuela Fortes
# 188790
a = str(input('1ª string: '))
b = str(input('2ª string: '))
if b not in a:
    print(f'{b} não encontrado em {a}')
else:
    position = a.find(b)
    print(f'{b} encontrado na posição {position} de {a}')