import sys

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    ans_array = []
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            for l in range(j+1, len(input_list)):
                ans_array.append(input_list[i]+input_list[j]+input_list[l])

    result = 0
    for i in sorted(ans_array):
        # print(result, ans_array[i])
        if i <= y:
            result = i
    print(result)


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
arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))


answer(n, m, arr)

