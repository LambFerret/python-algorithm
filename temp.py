arr = [0] * 20
arr[0], arr[1] = 1, 1
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = arr[i - 2] + arr[i - 1]
arr = [0] + arr
print(arr[int(input())])