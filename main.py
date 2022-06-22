import sys

# init

n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    sorted_list = sorted(list(set(input_list)))
    a = {sorted_list[i]: i for i in range(len(sorted_list))}
    result1 = [a[i] for i in input_list]
    return result1
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


result = answer(n, m, arr)

for a in result:
    print(a)
