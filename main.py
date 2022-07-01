import sys
from collections import deque

# init
n, m, k, arr = 0, 0, 0, []


# constant
class AC:
    def __init__(self, initq):
        self.q = deque(initq)
        self.is_reverse = False

    def D(self):
        if not self.is_reverse:
            self.q.popleft()
        else:
            self.q.pop()

    def R(self):
        self.is_reverse = not self.is_reverse


def makeAC(ls: list):
    try:
        ac = AC(ls[2])
        for i in ls[0]:
            if i == 'D':
                ac.D()
            elif i == 'R':
                ac.R()
        a = list(map(int, ac.q))
        if ac.is_reverse:
            a.reverse()
        return str(a).replace(' ','')
    except IndexError:
        return 'error'


def answer(x, y, input_list):
    ans = []
    for i in input_list:
        ans.append(makeAC(i))

    return ans
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
# arr = list(map(int, sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))

# list<int>를 n줄 받은 경우
# for _ in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))

# list<str>를 n줄 받은 경우
# for _ in range(n):
#     arr.append(list(map(str, sys.stdin.readline().split())))

# 번외 : list<str>를 3n줄 신기하게 받은 경우
for _ in range(n):
    # a = sys.stdin.readline().split()
    temp = [
        sys.stdin.readline().replace('\n', ''), int(sys.stdin.readline())
    ]
    if temp[1] == 0:
        sys.stdin.readline()
        temp.append([])
    else:
        temp.append(sys.stdin.readline().replace('\n', '').replace('[', '').replace(']', '').split(','))
    arr.append(temp)
    # arr.append(list(map(str, sys.stdin.readline().split())))

# list<int>를 특정 문자열 까지 받는 경우
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data == '.':
#         break
#     arr.append(data)

# str를 특정 문자열 까지 받는 경우
# while True:
#     data = sys.stdin.readline().replace('\n', '')
#     if data == '.':
#         break
#     arr.append(data)

result = answer(n, m, arr)
# print(result)
for i in result:
    print(i)
