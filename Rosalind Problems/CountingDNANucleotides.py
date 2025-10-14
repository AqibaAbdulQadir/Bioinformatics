from collections import Counter

s = input()
c = Counter(s)
for r in ['A', 'C', 'G', 'T']:
    print(c[r], end=' ')