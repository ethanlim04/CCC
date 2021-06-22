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
while(count < 9999):
    tttemp = []
    prev_factors = []

    for p in range(len(factors)):
        for q in range(len(factors[p])):
            tttemp.append(factors[p][q])
        prev_factors.append(tttemp)
    
    next_numbers = []

    for i in numbers:
        [ttemp, factors] = checkForFactor(i, factors, board)

        for j in ttemp:
            next_numbers.append(j)
    numbers = next_numbers
    
    if(factors[-1][-1] == True):
        doable = True
        break
    elif(prev_factors == factors):
        doable = False
        break
    count += 1


if(doable == True):
    print("yes")
else:
    print("no")
