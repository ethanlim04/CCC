n = int(input(""))
arr = list()
for i in range(n):
    arr.append(input("").split(' '))
    arr[i][0] = int(arr[i][0])
    arr[i][1] = int(arr[i][1])
arr.sort()
speeds = list()
for i in range(n):
    try:
        speeds.append(abs((arr[i+1][1]-arr[i][1]) / (arr[i+1][0]-arr[i][0])))
    except:
        continue
print(max(speeds))