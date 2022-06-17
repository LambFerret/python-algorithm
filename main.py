import sys

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    ans = []
    for i in range(x):
        process = sum(list(map(int, list(str(i)))))
        # print(x,i, process, i+process,  x == i+process)
        if x == i+process:
            return i
    return 0

    # print(x, y, input_list)


"""N, M Input"""
# 숫자 n을 받은 경우
n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
# n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
for _ in range(n):
    arr.append(sys.stdin.readline().split())


# int를 한줄에 받은 경우
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))


a = answer(n, m, arr)
print(a)

