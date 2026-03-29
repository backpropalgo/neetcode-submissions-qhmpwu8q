class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts.update({n : 1})
        r = [s[0] for s in sorted(counts.items(), key=lambda item:item[1], reverse=True)]
        return r[:k]
        