s = input()
res = []
for r in s:
    if r == 'A': res.append('T')
    elif r == 'C': res.append('G')
    elif r == 'G': res.append('C')
    elif r == 'T': res.append('A')
print(''.join(res[::-1]))
