def two_sum(nums, t):
    myDict = {}
    for i in range(len(nums)):
        val = t - nums[i]
        if val in myDict:
            return (myDict.get(val), i)
        myDict[nums[i]] = i

print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
print(two_sum([3, 3], 6))           # (0, 1)