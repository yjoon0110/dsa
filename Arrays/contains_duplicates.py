def containsDuplicate(nums):
    sample=set()
    # if nums is None:
        # return False
    for num in nums:
        if num in sample:
            return True
        sample.add(num)
    return False

# nums = [2, 7, 11, 15, 7]
nums = []

print(containsDuplicate(nums))

