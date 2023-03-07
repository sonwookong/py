n = int(input())

mat = [[0 for i in range(n)] for j in range(n)]
nap = 'right'
s, c = 0, 0

for i in range(1, n**2+1):
    mat[s][c] = i
    if nap == 'right':
        if mat[s][c - n + 1] == 0:
            c += 1
        else:
            nap = 'down'
            s += 1
    elif nap == 'down':
        if mat[s - n + 1][c] == 0:
            s += 1
        else:
            nap = 'left'
            c -= 1
    elif nap == 'left':
        if mat[s][c - 1] == 0:
            c -= 1
        else:
            nap = 'up'
            s -= 1
    elif nap == 'up':
        if mat[s - 1][c] == 0:
            s -= 1
        else:
            nap = 'right'
            c += 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()


