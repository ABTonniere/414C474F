max = 2000000000
min = 1

while True:
    mid = ((max-min)// 2) + min
    print(mid)
    rep = input()
    if rep == "TROPFROID":
        min = mid + 1
    elif rep == "TROPCHAUD":
        max = mid - 1
    else:
        break