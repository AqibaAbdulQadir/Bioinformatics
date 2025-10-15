maxi = 0
name1 = input()
main = name2 = s = ''
while True:
    curr = s = ''
    while not curr or curr[0] != '>':
        s += curr
        curr = input()
        if curr == '': break
    name2 = curr
    gc = (s.count("C") + s.count("G")) / len(s)
    if gc > maxi:
        main = name1
        maxi = gc
    name1 = name2
    if curr == '': break

print(main[1:])
print(maxi*100)


