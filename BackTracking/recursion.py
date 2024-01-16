p = 0
for j in range(100):
    for i in range(j):
        print(j)
        if j % 3 == 0:

            q = i + 4 if j < 40 else None

        else:

            q = i + 40

        p += float(q) / 1000