class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_counts = [0] * 26
        word_groups = {}
        for w in strs:
            cur_map = [0] * 26
            for c in w:
                i = ord(c) - 97
                cur_map[i] += 1
            k = '-'.join(str(n) for n in cur_map)
            if k in word_groups:
                word_groups[k].append(w)
            else:
                word_groups[k] = [w]
        return [v for v in word_groups.values()]
                

       
        
        
            