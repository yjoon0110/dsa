
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


def two_sum(nums, target):
    sample = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in sample:
            return (sample.get(val), i)
        sample[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
nums = [3, 3]
target = 6
print(two_sum(nums, target))  # Output: [0, 1]

