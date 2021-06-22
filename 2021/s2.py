m = int(input())
n = int(input())
k = int(input())
choicesR = {}
choicesC = {}
for i in range(k):
    temp = input().split(" ")
    if(temp[0] == "R"):
        choicesR[temp[1]] = (choicesR.setdefault(temp[1], 0) + 1)%2
    else:
        choicesC[temp[1]] = (choicesC.setdefault(temp[1], 0) + 1)%2
rTotal = 0
cTotal = 0
for key in choicesR:
    if(choicesR[key] == 1):
        rTotal += 1
for key in choicesC:
    if(choicesC[key] == 1):
        cTotal += 1
total = (rTotal * n) + (cTotal * m) - 2*rTotal*cTotal
print(total)