'''
import sys

sys.setrecursionlimit(10_000)
'''
'''
n = 3
m = 4
board = [
    [3, 10, 8, 14],
    [1, 11, 12, 12],
    [6, 2, 3, 9]
]
'''
n = int(input(""))
m = int(input(""))
board = []
for k in range(n):
    temp = input().split(" ")
    for q in range(m):
        temp[q] = int(temp[q])
    board.append(temp)

factors = list()
for i in range(n):
    temp = []
    for j in range(m):
        temp.append((i+1)*(j+1))
    factors.append(temp)

def checkForFactor(p, factors, board):
    numbers = []
    for i in range(n):
        for j in range(m):
            if(factors[i][j] == p):
                factors[i][j] = True
                numbers.append(board[i][j])
    return [numbers, factors]

[numbers, factors] = checkForFactor(board[0][0], factors, board)
count = 0
doable = False

def iterFunc(numbers, factors, board, count):
    if(count > 99999):
        return False
    tempList = []
    prev_factors = []
    numbers2 = []
    for p in range(len(factors)):
        for q in range(len(factors[p])):
            tempList.append(factors[p][q])
        prev_factors.append(tempList)

    for i in numbers:
        [numbers2, factors] = checkForFactor(i, factors, board)
        if(factors[-1][-1] == True):
            return True
        elif(prev_factors == factors):
            #print("fuck")
            continue
        else:
            #print("recurse")
            #print(factors)
            return iterFunc(numbers2, factors, board, count+1)
#print(numbers)
doable = iterFunc(numbers, factors, board, 0)
if(doable == True):
    print("yes")
else:
    print("no")
