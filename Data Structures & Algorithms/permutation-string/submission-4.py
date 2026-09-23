class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        set_of_s1 = set(s1)
        dict_of_s1 = defaultdict(int)
        for letter in s1:
            dict_of_s1[letter] += 1
        print(dict_of_s1)
        while r < len(s2):
            while r < len(s2) and dict_of_s1[s2[l]] == 0:
                l += 1
                r += 1
            temp_dict = defaultdict(int)
            for letter in s2[l:r+1]:
                temp_dict[letter] += 1 
            # print("temp: ")
            # print(temp_dict)
            # print("of_s1: ")
            # print(dict_of_s1)
            # clean_dict_of_s1 = [k for k, v in dict_of_s1.items() if v != 0]
            # clean_temp_dict = [k for k, v in temp_dict.items() if v != 0]
            # print("c temp: ")
            # print(clean_temp_dict)
            # print("c of_s1: ")
            # print(clean_dict_of_s1)
            is_same = True
            for k, v in dict_of_s1.items():
                if temp_dict[k] != v:
                    is_same = False
                    break
            if is_same:
                print(temp_dict)
                return True
            else:
                l += 1
                r += 1
            
        return False

            