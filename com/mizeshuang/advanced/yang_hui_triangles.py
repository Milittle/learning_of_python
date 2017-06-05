def triangles():
    p = [1]
    a = 0
    while True:
        q = []
        i = 0
        while i <= a:
            if i == 0 or i == len(p):
                q.append(1)
            else:
                q.append(p[i-1]+p[i])
            i += 1
        p = q
        yield q
        a += 1
def triangles1():
    p = [1]
    while True:
        yield p
        p.insert(0,0)
        p.append(0)
        p = [p[i] + p[i + 1] for i in range(len(p)-1)]
g = triangles1()
n = 0
for i in g:
    print(i)
    n +=1
    if n == 10:
        break