class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        dict_of_s1 = defaultdict(int)
        temp_dict = defaultdict(int)

        for letter in s1:
            dict_of_s1[letter] += 1
        for letter in s2[l:r+1]:
            temp_dict[letter] += 1

        while r < len(s2):
            # while r < len(s2) and dict_of_s1[s2[l]] == 0:
            #     l += 1
            #     r += 1
            #     temp_dict[s2[l-1]] -= 1
            #     if r != len(s2):
            #         temp_dict[s2[r]] += 1

            
            if dict_of_s1 == temp_dict:
                return True
            else:
                l += 1
                r += 1
                if r < len(s2):
                    temp_dict[s2[l-1]] -= 1
                    if temp_dict[s2[l-1]] == 0:
                        del temp_dict[s2[l-1]]
                    temp_dict[s2[r]] += 1
                
        return False
