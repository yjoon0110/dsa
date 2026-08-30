def valid_anagram(nums, t):
    if len(nums) != len(t):
        return False
    
    freq = [0] * 26
    for i in range(len(nums)):
        c1 = nums[i]
        c2 = t[i]
        freq[ord(c1) - ord('a')]+=1
        freq[ord(c2) - ord('a')]-=1

    for num in freq:
        if num != 0:
            return False
    
    return True


print(valid_anagram("anagram", "nagaram"))  # True
print(valid_anagram("rat", "car"))          # False