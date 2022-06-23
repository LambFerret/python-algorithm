N = 'g1'
alpha = ['a','b','c','d','e','f','g','h']
x = alpha.index(N[0])
y = int(N[1])
checkmate = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
count =0
for a in checkmate:
    x1 =x+ a[0]
    y1 =y+ a[1]
    if x1>0 and y1>0 and x1<8 and y1<8:
        count+=1

print(count)