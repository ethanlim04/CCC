def store_euclid(x, y, outArr):
    r = y%x
    q = int(y/x)
    outArr.append([r, y, {q: x}])
    if(r == 0):
        return outArr
    else:
        return store_euclid(r, x, outArr)

def rev_euclid(inArr, x, y):
    out = inArr[-1]
    for i in range(len(inArr)):
        #r = y - q*x
        #[r, y, q, x]
        outArr[0] = 0

n = int(input())
p = []
w = []
d = []
for i in range(n):
    [a, b, c] = input().split(" ")
    p.append(int(a))
    w.append((1/int(b)))
    d.append(int(c))
print(p, w, d)

total = {}
sortArrA = []
sortArrB = []
for i in range(n):
    total[p[i] - d[i] - w[i]] =  {p[i] - d[i]: -w[i]}
    total[p[i] + d[i] + w[i]] =  {p[i] + d[i]: w[i]}
    sortArrA.append(p[i] - d[i] - w[i])
    sortArrB.append(p[i] + d[i] + w[i])
sortArrA.sort()
sortArrB.sort()
highPoint = (total[sortArrA[-1]])
lowPoint = (total[sortArrB[0]])
factList = store_euclid(min(1/lowPoint[key], 1/maxPoint[key]), max(1/lowPoint[key], 1/maxPoint[key]))
times = rev_euclid(factList, min(1/lowPoint[key], 1/maxPoint[key]), max(1/lowPoint[key], 1/maxPoint[key]))
print(total)