T = int(input())
for i in range(T):
    gifts = int(input().strip())
    _4_gifts = gifts / 5
    if _4_gifts >= 1:
        print(gifts - int(_4_gifts))
    else:
        print(gifts)
