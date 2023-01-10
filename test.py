a = int(input("Podaj liczbę: ")) # 1 * t_1

for i in range(a):               # n * t_2
    print(i)                     # 1 * t_3
    a*=i                         # 1 * t_4

print(a)                         # 1 * t_5

# t_1 = t_3