# Manuela Fortes
# 188790
max = -40
min = 100
for i in range(12):
    x = float(input())
    if x > max:
        max = x
    if x < min:
        min = x
print(max-min)