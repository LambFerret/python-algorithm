import sys
import math
from collections import Counter

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    input_list.sort()
    print(round(sum(input_list) / len(input_list)))
    print(input_list[math.floor(len(input_list) / 2)])
    c = Counter(input_list).most_common()
    if len(c) > 1:
        for i in range(len(c)):
            if c[i][1] == c[i + 1][1]:
                print(c[i + 1][0])
                break
            else:
                print(c[i][0])
                break
    else:
        print(arr[0])

    return max(input_list) - min(input_list)
    return (x, y, input_list)


"""N, M Input"""
# 숫자 n을 받은 경우
n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
# n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
# for _ in range(n):
#     arr.append(sys.stdin.readline().replace('\n', ''))

# int를 한줄에 받은 경우
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
for _ in range(n):
    arr.append(int(sys.stdin.readline().replace('\n', '')))

print(answer(n, m, arr))
