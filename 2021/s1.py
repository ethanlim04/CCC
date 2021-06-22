n = int(input())
lengths = input().split(" ")
widths = input().split(" ")

for i in range(len(lengths)):
    lengths[i] = int(lengths[i])
for j in range(len(widths)):
    widths[j] = int(widths[j])

s = 0
for k in range(n):
    s += ((lengths[k] + lengths[k+1])*widths[k])
print(s/2)