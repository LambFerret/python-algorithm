import sys
import math
from collections import Counter

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    input_list.sort()

    for i in input_list:
        print(i[1],i[0])

    return (x, y, input_list)


"""N, M Input"""
# 숫자 n을 받은 경우
n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
# n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
for _ in range(n):
    list_a = sys.stdin.readline().replace('\n', '').split()
    list_a.reverse()
    arr.append(tuple(map(int,list_a)))

# int를 한줄에 받은 경우
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))

answer(n,m,arr)
# print(answer(n, m, arr))
