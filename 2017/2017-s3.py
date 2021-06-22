n = int(input())
nums = input().split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()
minLen = nums[0] + nums[1]
maxLen = nums[-1] + nums[-2]
out = {}
maxVal = 0

def baseNums(numsList, length):
    count = 0
    for elem in numsList:
        inverse = length-elem
        if(inverse in numsList):
            numsList.remove(elem)
            numsList.remove(inverse)
        else:
            numsList.remove(elem)
            count += 1
    return count

if(minLen == maxLen):
    print(int((n - baseNums(nums, minLen))/2), 1)
else:
    for length in range(minLen, maxLen-1):
        res = int((n - baseNums(nums, length))/2)
        maxVal = max(res, maxVal)
        out.setdefault(res, set()).add(length)
        print(out)
    print(maxVal, len(out[maxVal]))