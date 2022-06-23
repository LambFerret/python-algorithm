
n, m = map(int, input().split())
ls = []
for a in range(n):
    b = min(map(int, input().split()))
    ls.append(b)
print(max(ls))