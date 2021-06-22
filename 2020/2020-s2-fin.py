import sys

sys.setrecursionlimit(300_000)
#sys.setrecursionlimit(500_000)

'''
m = 3
n = 4
t = [
    [3, 10, 8, 14],
    [1, 11, 12, 12],
    [6, 2, 3, 9]
]
'''
'''
m = 2
n = 2
t = [
    [2, 77],
    [55, 3]
]
'''


'''
m = int(input(""))
n = int(input(""))
t = []
for k in range(m):
    temp = input().split(" ")
    for q in range(n):
        temp[q] = int(temp[q])
    t.append(temp)
'''

rows = int(sys.stdin.readline())  # No. of rows
columns = int(sys.stdin.readline())  # No. of columns
board = {}
for i in range(rows):
    vals = list(
        map(int, sys.stdin.readline().split())
    )  # Split input by space and convert values to an integer

    for index, val in enumerate(vals):  # Add squares to the squares dictionary
        squareValue = (i + 1) * (index + 1)
        board.setdefault(val, []).append(squareValue)
print(board)
'''
board = {}
for i in range(m):
    for j in range(n):
        
        #if(t[i][j] in board):
        #    board[t[i][j]].append((i+1)*(j+1))
        #else:
        #    board[t[i][j]] = [(i+1)*(j+1)]
        
        board.setdefault(t[i][j], []).append((i+1)*(j+1))
'''
global searchedKeys
#sets are faster to search than lists
searchedKeys = set()

def recurse(searchArr):
    for key in searchArr:
        if(key in searchedKeys):
            pass
        else:
            searchedKeys.add(key)
            ttemp = board.setdefault(key, [])
            if(1 in ttemp):
                return True
            #return breaks function
            #return recurse(board, ttemp, searchedKeys)
            if(recurse(ttemp)):
                return True
    return False

res = recurse([rows*columns])
print("yes" if res else "no")