def top_k_freq_ele(nums, k):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else: freq[num]+=1

    bucket = [[] for _ in range(len(nums)+1)]

    for key, val in freq.items():
        bucket[val].append(key)

    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result