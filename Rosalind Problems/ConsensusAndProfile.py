from collections import defaultdict
x = input()
dct = defaultdict(lambda: {'A':0, 'C':0, 'G':0, 'T':0})
while x:
    s = ''
    st = input()
    while st and st[0] != '>':
        s += st
        st = input()
    if s:
        for i, c in enumerate(s):
            dct[i][c] += 1
    x = st
maxi = []
for key in dct:
    lst = sorted(list(dct[key].items()), key=lambda x: x[1])
    maxi.append(lst[-1][0])
print(''.join(maxi))
for char in ['A', 'C', 'G', 'T']:
    print(f'{char}: {" ".join([str(dct[key][char]) for key in range(len(dct))])}')

