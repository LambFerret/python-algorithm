import sys

# init
n, m, k, arr = 0, 0, 0, []


# constant


def answer(x, y, input_list):
    ans_array = []
    for i in range(len(input_list)):
        count = 0
        for j in range(len(input_list)):
            if input_list[i][0]<input_list[j][0] and input_list[i][1]<input_list[j][1]:
                count+=1
        ans_array.append(count+1)

    return ans_array
    return (x,y,input_list)

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
    arr.append(list(map(int,(sys.stdin.readline().split()))))


# int를 한줄에 받은 경우
# arr = list(map(int,sys.stdin.readline().split()))

# int를 n줄 받은 경우
# for _ in range(n):
#     arr.append(int(sys.stdin.readline().replace('\n', '')))


a = answer(n, m, arr)
for i in a:
    print(i)

