T = int(input())
for i in range(T):
    items = input().split(" ")
    n = int(items[0])
    b = float(items[1])
    res = []
    is_found = False
    for j in range(n):
        _items = input().split(" ")
        w = int(_items[0])
        h = int(_items[1])
        p = int(_items[2])
        res.append((w*h, p))
        if p <= b:
            is_found = True

    if not is_found:
        print("no tablet")
    else:
        sorted_list = sorted(res, key=lambda k: k[0], reverse=True)
        for m in sorted_list:
            if m[1] <= b:
                print(m[0])
                break
