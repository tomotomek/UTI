ret = "01"
for i in range(5):
    pom = ""
    for j in range(len(ret)):
        if ret[j] == '0':
            pom += '1'
        else:
            pom += '0'
    ret += pom

import turtle, time

t = turtle.Turtle()
turtle.tracer(0,0)
t.pu()
t.setpos(300,290)
t.pd()

def znak(i, j):
    j+=1
    pocet = 0
    while i > 2:
        i = i//2
        if j > i:
            pocet += 1
            j = j-i
    if pocet % 2 == 0:
        return j-1
    else:
        if j-1 == 0:
            return 1
        else:
            return 0

t_start = time.time()

for i in range(2**30):
    pohyb = znak(2**10, i)
    if pohyb == 0:
        t.fd(2)
    else:
        t.lt(60)
        
print(time.time() - t_start)
turtle.update()
