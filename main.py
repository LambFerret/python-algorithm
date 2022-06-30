import sys
from collections import deque
# init

n, m, k, arr = 0, 0, 0, []


# constant
class Queue:
    def __init__(self):
        self.queue = deque()

    def push_front(self, x):
        self.queue.appendleft(x)

    def push_back(self, x):
        self.queue.append(x)

    def pop_front(self):
        if not self.queue:
            return -1
        else:
            return self.queue.popleft()

    def pop_back(self):
        if not self.queue:
            return -1
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        return 0 if len(self.queue) != 0 else 1

    def front(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if not self.queue:
            return -1
        else:
            return self.queue[-1]


def answer(x, y, input_list):
    queue = Queue()
    for i in input_list:
        if i[0] == 'push_back':
            queue.push_back(i[1])
        elif i[0] == 'push_front':
            queue.push_front (i[1])
        elif i[0] == 'pop_front':
            print(queue.pop_front())
        elif i[0] == 'pop_back':
            print(queue.pop_back())
        elif i[0] == 'size':
            print(queue.size())
        elif i[0] == 'empty':
            print(queue.empty())
        elif i[0] == 'front':
            print(queue.front())
        elif i[0] == 'back':
            print(queue.back())

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
for _ in range(n):
    arr.append(list(map(str, sys.stdin.readline().split())))

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
# for i in result:
#     print(i)
