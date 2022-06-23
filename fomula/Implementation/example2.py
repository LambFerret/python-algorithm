N = 5
count = 0
for a in range(1, N + 1):
    for b in range(1, 61):
        for c in range(1, 61):
            if "3" in list(str(a) + str(b) + str(c)):
                count += 1

print(count)
