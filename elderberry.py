import math

inp = input()

a = float(inp.split()[0])
b = float(inp.split()[1])
c = float(inp.split()[2])

maxnum = max(a, b, c)
max_ratio = 0

if (b == maxnum):
    max_ing = 'b'
    max_ratio = 12
elif (c == maxnum):
    max_ing = 'c'
    max_ratio = 40
else:
    max_ing = 'a'
    max_ratio = 12

fin_ratio = maxnum / max_ratio

fin_a = (fin_ratio * 12) - a
fin_b = (fin_ratio * 12) - b
fin_c = (fin_ratio * 40) - c

print(float(fin_a), float(fin_b), float(fin_c))

