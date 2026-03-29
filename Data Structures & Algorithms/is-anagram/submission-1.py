class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counts_s = {}
        char_counts_t = {}
        for char in s:
            if char not in char_counts_s:
                char_counts_s[char] = 1
            else:
                char_counts_s[char] += 1

        for char in t:
            if char not in char_counts_t:
                char_counts_t[char] = 1
            else:
                char_counts_t[char] += 1
        
        return char_counts_s == char_counts_t
        
        