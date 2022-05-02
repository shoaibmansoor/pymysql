T = int(input())
for i in range(T):
    items = input().split(" ")
    quantity = int(items[0])
    price = float(items[1])
    total = price * quantity
    if quantity > 1000:
        total = total * 0.9

    print(format(total, '.6f'))