import sys

# init

n, m, k, arr = 0, 0, 0, []

# constant
joystick = ['', (1, 0), (-1, 0), (0, -1), (0, 1)]


def answer(x, y, input_list):
    max_width = 0
    max_height = 0
    for i in input_list:
        if i[0] >2 and max_width<i[1]:
            max_width = i[1]
        if i[0] <3 and max_height<i[1]:
            max_height = i[1]
    input_list = input_list+ input_list
    small_square = 0
    for i in range(len(input_list)):
        if input_list[i][1] in [max_width, max_height] and input_list[i+1][1] in [max_width, max_height]:
            small_square = input_list[i+3][1] * input_list[i+4][1]
            break
    return x * (max_width*max_height - small_square)

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
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))

# list<int>를 n줄 받은 경우
for _ in range(6):
    arr.append(list(map(int, sys.stdin.readline().split())))

# int를 특정 문자열 까지 받는 경우
# while True:
#     data = list(map(int, sys.stdin.readline().split()))
#     if data == [0, 0, 0]:
#         break
#     arr.append(data)

result = answer(n, m, arr)

print(result)
