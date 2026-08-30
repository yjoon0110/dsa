
def group_anagram(s):
    

    sample = {}

    for word in s:
        freq = [0] * 26
        for i in range(len(word)):
            c = word[i]
            freq[ord(c) - ord('a')]+=1
        if tuple(freq) in sample:
            sample[tuple(freq)].append(word)
        else:
            sample[tuple(freq)] = [word]


    return sample.values()

print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
