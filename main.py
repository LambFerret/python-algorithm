import sys
from collections import deque

# init
n, m, k, arr = 0, 0, 0, []


# constant
class RoundDeque:
    def __init__(self, initq):
        self.q = deque(initq)
        self.count = 0

    def pop(self):
        return self.q.popleft()

    def move_left(self):
        self.count += 1
        self.q.append(self.pop())

    def cursor(self):
        return self.q[0]


def answer(x, y, input_list):
    q = RoundDeque(range(1, x + 1))
    count = 0
    for target_number in input_list:
        while target_number != q.cursor():
            q.move_left()
        count += min(q.count, len(q.q)-q.count)
        q.pop()
        q.count = 0




    return count
    return x, y, input_list


"""N, M Input"""
# 숫자 n을 받은 경우
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
n, m = map(int, sys.stdin.readline().split())

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
#     arr.append(list(map(str, sys.stdin.readline().split())))

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
print(result)
# for i in result:
#     print(i)
