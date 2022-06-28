import sys

# init

n, m, k, arr = 0, 0, 0, []


# constant
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        return ('+')

    def pop(self):
        return self.stack.pop(-1)

        # return a


def answer(x, y, input_list):
    ans = []
    s = Stack()
    is_correct = True
    i = 1
    while input_list:
        if i <= input_list[0]:
            ans.append(s.push(i))
            i += 1
            # print('아직 작음 ㄱ', input_list)
            # print('아직 작음 ㄴ', i)
            # print('아직 작음 ㄷ', s.stack)
            continue
        if i > input_list[0]:
            # print('정답 ㄱ', input_list)
            # print('정답 ㄴ', i)
            # print('정답 ㄷ', s.stack)
            spop = s.pop()
            inputpop = input_list.pop(0)
            if spop != inputpop:
                is_correct = False
            ans.append(spop)
    if is_correct:
        for al in ans:
            print('+' if al == '+' else '-')
    else:
        print('NO')
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
for _ in range(n):
    arr.append(int(sys.stdin.readline().replace('\n', '')))

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
