def soch(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    return soch(n - 1, k) + soch(n - 1, k - 1)


n, k = map(int, input().split())
print(soch(n, k))
