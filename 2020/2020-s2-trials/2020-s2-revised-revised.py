import sys

sys.setrecursionlimit(300_000)

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
        temp.append(False)
    factors.append(temp)

def check(board, factors, val):
    out = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == val):
                out.append((i+1)*(j+1))
                factors[i][j] = True
    return [out, factors]

def iterFunc(board, factors, vals, count):
    ttemplist = []
    
    for i in vals:
        prev_fact = hash(str(factors))
        values = []
        [values, factors] = check(board, factors, i)
        if factors[0][0] == True:
            return True
        elif(prev_fact == hash(str(factors))):
            continue
        else:
            return iterFunc(board, factors, values, count+1)

    return False

print("yes" if iterFunc(board, factors, [m*n], 0) else "no")