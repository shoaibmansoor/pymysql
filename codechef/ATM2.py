T = int(input())
for i in range(T):
    items = input().split(" ")
    n = int(items[0])
    k = int(items[1])
    need_m = list(map(lambda e: int(e), input().split(" ")))
    res = []
    for j in need_m:
        if (k - j) >= 0:
            res.append('1')
            k = k - j
        else:
            res.append('0')
    print(' '.join(res))

