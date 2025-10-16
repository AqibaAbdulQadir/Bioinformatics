s = input()
m = input()
l, n = len(m), len(s)
i = 0
ans = []
while i < n - l:
    while i < n and s[i] != m[0]: i += 1
    j, stop = 0, i + l
    while i < n and i + j < stop:
        if m[j] == s[i+j]: j += 1
        else: break
    if i + j == stop: ans.append(str(i+1))
    i += 1
print(' '.join(ans))



