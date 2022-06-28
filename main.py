import math
import sys

# init

n, m, k, arr = 0, 0, 0, []


# constant
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        try:
            return self.stack.pop(-1)
        except IndexError:
            return -1

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return 0 if len(self.stack)>0 else 1

    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            return -1


def answer(x, y, input_list):
    s = Stack()
    for i in input_list:
        if i[0] == 'push':
            s.push(i[1])
        elif i[0] == 'pop':
            print(s.pop())
        elif i[0] == 'size':
            print(s.size())
        elif i[0] == 'empty':
            print(s.is_empty())
        elif i[0] == 'top':
            print(s.top())

    # return x, y, input_list


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

# list<str>를 n줄 받은 경우
for _ in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))

# int를 특정 문자열 까지 받는 경우
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data == [0, 0, 0]:
#         break
#     arr.append(data)

result = answer(n, m, arr)
# for a in result:
#     print(a)
