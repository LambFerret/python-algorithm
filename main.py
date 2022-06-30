import sys
from collections import deque

# init
n, m, k, arr = 0, 0, 0, []


# constant

def answer(x, y, input_list):
    ans = []
    for i in range(x):
        i = i * 2
        a, b = input_list[i]
        i_list = [0] * a
        i_list[b] = 1
        q = deque(input_list[i + 1])
        qi = deque(i_list)
        is_answer = False
        count = 0
        while not is_answer:
            large = max(q)
            loop_a = q.popleft()
            loop_b = qi.popleft()
            if loop_b == 1 and large == loop_a:
                count += 1
                is_answer = True
            else:
                if loop_a == large:
                    count += 1
                else:
                    q.append(loop_a)
                    qi.append(loop_b)
        ans.append(count)
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
for _ in range(2 * n):
    arr.append(list(map(int, sys.stdin.readline().split())))

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
# print(result)
for i in result:
    print(i)
