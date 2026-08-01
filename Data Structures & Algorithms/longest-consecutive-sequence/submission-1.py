class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        final_longest = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                longest = 0
                i = n
                while i in nums_set:
                    longest += 1
                    i += 1
                if longest > final_longest:
                    final_longest = longest
                
                


        return final_longest
        