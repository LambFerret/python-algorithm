import sys

# init
n, m, k, arr = 0, 0, 0, []
strbuilder = ''
w = 0
b = 0
# constant
def answer(x, y, input_list):
    recursive(0, 0, x)

    # return x, y, input_list
    return w, b

def recursive(x1, y1, length):
    global w, b, arr, strbuilder
    unit = arr[x1][y1]
    for i in range(x1, x1+length):
        for j in range(y1, y1+length):
            if unit != arr[i][j]:
                strbuilder += '('

                recursive(x1, y1, length // 2)
                recursive(x1, y1 + length // 2, length // 2)
                recursive(x1 + length // 2, y1, length // 2)
                recursive(x1 + length // 2, y1 + length // 2, length // 2)
                strbuilder += ')'

                return;
    if unit == '0':
        strbuilder += '0'

        w += 1
    else:
        strbuilder += '1'

        b += 1


"""N, M Input"""
# 숫자 n을 받은 경우
n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
# n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
for _ in range(n):
    arr.append(sys.stdin.readline().replace('\n', ''))


# int를 한줄에 받은 경우
# arr = list(map(int, sys.stdin.readline().split()))

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
# print(result)
# for i in result:
#     print(i)
print(strbuilder)