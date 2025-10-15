k, m, n = list(map(int, input().strip().split()))
t = k+m+n
print(k/t + m/t*(k/(t-1) + 0.75*(m-1)/(t-1) + 0.5*(n/(t-1))) + n/t*(k/(t-1) + 0.5*m/(t-1)))
