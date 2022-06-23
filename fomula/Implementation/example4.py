max_map = (4, 4)
x, y, face = (1, 1, 0)

world = [[1, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 1, 0, 1],
         [1, 0, 0, 1]]

joystick = [[1, 0], [-1, 0], [0, -1], [0, 1]]

steps = []
for b in range(5):
    for a in joystick:
        nx = x + a[0]
        ny = y + a[1]
        if world[ny][nx] == 0:
            steps.append((x, y, nx, ny))
            world[ny][nx] = 1
            x, y = nx, ny

print(steps)
