import sys

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    least_array = []
    who_is_first = ['WBWBWBWB', 'BWBWBWBW']
    first = ''
    for c in range(2):
        first = True if c else False
        for i in range(x - 7):
            for j in range(y - 7):
                count = 0
                for a in range(8):
                    for b in range(8):
                        compare = who_is_first[0] if first else who_is_first[1]
                        if compare[b] != input_list[i + a][j + b]:
                            count += 1
                    first = not first
                least_array.append(count)
    return int(min(least_array))
    return (x, y, input_list)

    # print(x, y, input_list)


"""N, M Input"""
# 숫자 n을 받은 경우
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# 숫자 n, m을 받은 경우
n, m = map(int, sys.stdin.readline().split())

"""List Input"""
# string을 n줄 받는 경우
for _ in range(n):
    arr.append(sys.stdin.readline().replace('\n', ''))

# int를 한줄에 받은 경우
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))


print(answer(n, m, arr))
