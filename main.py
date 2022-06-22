import sys
from collections import Counter
# init

n, m, k, arr = 0, 0, 0, []
arr2 = []


# constant


def answer(x, y, input_list):
    return x, y, input_list

def answer2(ls1, ls2):
    print(Counter(ls1).most_common()[1][0])
    print(Counter(ls2).most_common()[1][0])

    # return c[1],d[1]

"""N, M Input"""
# 숫자 n을 받은 경우
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
# n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
# for _ in range(n):
#     arr.append(sys.stdin.readline().replace('\n', ''))


# int를 한줄에 받은 경우
# arr = list(map(int, sys.stdin.readline().split()))

# int를 n줄 받은 경우
for _ in range(3):
    a, b = list(map(int, (sys.stdin.readline().split())))
    arr.append(a)
    arr2.append(b)

# result = answer(n, m, arr)
# print(result)

result = answer2(arr, arr2)
# print(result)