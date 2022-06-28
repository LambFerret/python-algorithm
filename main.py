import sys
import re

# init

n, m, k, arr = 0, 0, 0, []


# constant

def answer(x, y, input_list):
    ans = []
    for a in input_list:
        print(f(a))

    return x, y, input_list


def f(string):
    string = re.sub('[^()[\\]]', '', string)
    temp = []
    try:
        for b in string:
            if b == '(':
                temp.append(b)
            elif b == ')':
                if temp.pop(-1) != '(':
                    return 'no'
            elif b == '[':
                temp.append(b)
            elif b == ']':
                if temp.pop(-1) != '[':
                    return 'no'

        return 'yes' if len(temp) == 0 else 'no'
    except IndexError:
        return 'no'


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
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))

# list<int>를 n줄 받은 경우
# for _ in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))

# list<str>를 n줄 받은 경우
# for _ in range(n):
#     arr.append(list(map(str,sys.stdin.readline().split())))

# list<int>를 특정 문자열 까지 받는 경우
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data == '.':
#         break
#     arr.append(data)

# str를 특정 문자열 까지 받는 경우
while True:
    data = sys.stdin.readline().replace('\n', '')
    if data == '.':
        break
    arr.append(data)

result = answer(n, m, arr)

# print(result)
