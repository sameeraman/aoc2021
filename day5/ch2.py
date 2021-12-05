with open('input.txt') as f:
    lines = f.read().splitlines()

arraysize = 1000
import numpy as np

diagram = np.zeros([arraysize, arraysize]).astype(int)

for line in lines:
    x1y1, x2y2 = line.split(" -> ")
    x1,y1 = [int(xy) for xy in x1y1.split(',')]
    x2,y2 = [int(xy) for xy in x2y2.split(',')]

    # process only virticle or horizontal lines
    if (x1==x2 or y1==y2):
        if x1==x2:
            for y in range(min(y1,y2),max(y1+1,y2+1)):
                diagram[y][x1]+=1
        if y1==y2:
            for x in range(min(x1,x2),max(x1+1,x2+1)):
                diagram[y1][x]+=1
    else:
        x = range(x1,x2+1 if x2>x1 else x2-1,-1 if (x1>x2+1) else 1)
        print("x :" , list(x))
        y = range(y1,y2+1 if y2>y1 else y2-1,-1 if (y1>y2+1) else 1)
        print("y :" , list(y))
        for iterator in range(0,len(x)):
            diagram[y[iterator]][x[iterator]]+=1



print(diagram)
print("answer :", np.count_nonzero(diagram>=2))


