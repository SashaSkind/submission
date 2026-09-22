class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        # l = 0
        # r = 1
        # seen = set()
        # seen.add(s[l])
        # seen.add(s[r])
        # curr = 1
        # while r < len(s) - 1 and r >= l:
        #     while s[r] in seen:
        #         l += 1
        #         seen.remove(s[l])
        #     r += 1
        #     seen.add(s[r])
            
        #     if r - l + 1 > curr:
        #         curr = r - l + 1

        # return curr


        seen = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res






        # def lengthOfSubstring(string: str) -> int:
        #     count = 0
        #     seen = set()
        #     for letter in string:
        #         if letter in seen:
        #             break
        #         count += 1
        #         seen.add(letter)
        #     return count
        # length = len(s)
        # i = 0
        # maxx = 0
        # while i < length:
        #     if lengthOfSubstring(s[i:]) > maxx:
        #         maxx = lengthOfSubstring(s[i:])
        #     i += 1
        # return maxx
        