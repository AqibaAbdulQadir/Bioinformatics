def dna_needle_man(mat, A, B, i, j):
    ver = hor = diag = -float('inf')
    # print(i, j)
    if 1 <= i < len(mat) and 0 <= j < len(mat[0]):
        ver = mat[i-1][j][0] - 2
    if 0 <= i < len(mat) and 1 <= j < len(mat[0]):
        hor = mat[i][j-1][0] - 2
    if 1 <= i < len(mat) and 1 <= j < len(mat[0]):
        # print(i, j)
        if A[j] == B[i]:
            diag = mat[i-1][j-1][0] + 2
        else:
            diag = mat[i-1][j-1][0] - 1
    maxi = max([ver, hor, diag])
    ans = [ver == maxi, hor == maxi, diag == maxi]
    return [maxi, ans]
    # return maxi


def dna_water_man(mat, A, B, i, j):
    ver = hor = diag = 0
    if 1 <= i < len(mat) and 0 <= j < len(mat[0]):
        ver = max(0, mat[i-1][j][0] - 2)
    if 0 <= i < len(mat) and 1 <= j < len(mat[0]):
        hor = max(0, mat[i][j-1][0] - 2)
    if 1 <= i < len(mat) and 1 <= j < len(mat[0]):
        if A[j] == B[i]:
            diag = max(0, mat[i-1][j-1][0] + 2)
        else:
            diag = max(0, mat[i-1][j-1][0] - 1)

    maxi = max([ver, hor, diag])
    if maxi == 0: return [0, [False, False, False]]
    # print(maxi)
    ans = [ver == maxi, hor == maxi, diag == maxi]
    return [maxi, ans]


def dp_func(A, B, func):
    A, B = ' ' + A, ' ' + B
    dp = [[[0, [0, 0, 0]] for _ in range(len(A))] for _ in range(len(B))] # [val, ver, hor, diag]

    maxi = 0
    # Here, I'm initialising the base row and col
    for i in range(1, len(dp)):
        dp[i][0] = func(dp, A, B, i, 0)
    for j in range(1, len(dp[0])):
        dp[0][j] = func(dp, A, B, 0, j)

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = func(dp, A, B, i, j)
            maxi = max(maxi, dp[i][j][0])

    return dp, maxi


# print(dp_func("CAGGTAGTG", "CTAGTAG", dna_needle_man))
