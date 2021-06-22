n = int(input())
arr = list(map(int, input().split()))
arr.sort()
def getOut(n, arr, odd):
    out = []
    t1 = arr[0:int(n/2)]
    t2 = arr[int(n/2):n]
    t1 = t1[::-1]
    if(not odd):
        for i in range(int(n/2)):
            
            out.append(t1[i])
            out.append(t2[i])
    else:
        for i in range(int(n/2)):
            
            out.append(t2[i])
            out.append(t1[i])
    return out

if(n % 2 == 0):
    res = getOut(n, arr, False)
    print(*res)
else:
    output = []
    temp = int((n-1)/2)
    elem = arr[temp]
    #print(arr)
    arr.pop(temp)
    res = getOut(n-1, arr, True)
    output = [elem] + res
    print(*output)
