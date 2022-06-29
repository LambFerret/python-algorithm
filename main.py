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
        return self.stack.pop(-1)

    def peek(self, x):
        return self.stack[x]


def answer(x, y, input_list):
    ls = Stack()
    ans = [-1] * x
    ls.push(0)
    for i in range(1, x):
        while ls.stack and input_list[ls.peek(-1)] < input_list[i]:
            ans[ls.pop()] = input_list[i]
        ls.push(i)


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
arr = list(map(int, sys.stdin.readline().split()))

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
# while True:
#     data = sys.stdin.readline().replace('\n', '')
#     if data == '.':
#         break
#     arr.append(data)

result = answer(n, m, arr)
# print(result)
for i in result:
    print(i)
