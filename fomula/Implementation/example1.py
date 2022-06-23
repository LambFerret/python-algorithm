joystick = {
    'R': [1, 0],
    'L': [-1, 0],
    'U': [0, -1],
    'D': [0, 1],
}
N = 5  # map(int, input())
plan = ['R', 'L', 'L', 'L', 'L', 'R', 'R', 'R']  # list(input().split())
currentx, currenty = [1, 1]
for a in plan:
    x, y = joystick.get(a)
    currentx += x
    currenty += y
    currentx = N if currentx > N else currentx
    currenty = N if currenty > N else currenty
    currentx = 1 if currentx < 1 else currentx
    currenty = 1 if currenty < 1 else currenty

    if not (plan):
        break

print((currentx, currenty))
