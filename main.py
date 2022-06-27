import math
import sys

# init

n, m, k, arr = 0, 0, 0, []


# constant
PIE = math.pi
def answer(x, y, input_list):
    a = x**2 * PIE
    b = x**2 * 2
    return "{:.06f}".format(a), "{:.06f}".format(b)
    return x, y, input_list


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
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))

# list<int>를 n줄 받은 경우
# for _ in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))

# int를 특정 문자열 까지 받는 경우
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data == [0, 0, 0]:
#         break
#     arr.append(data)

result = answer(n, m, arr)
for a in result:
    print(a)
