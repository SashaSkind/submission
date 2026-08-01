from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        my_str = ""
        length = len(strs)
        count_str = " " * 100 
        my_list = []
        for s in strs:
            position = 0
            for l in s:
                my_str += l
                position += 1
            count_str = count_str + str(position) + (" " * 100)
        my_str = my_str + count_str + str(length)
        print(my_str)
        
        return my_str
                    
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []


        length = s[-1]
        print(f"len: {length}")
        s = s[:-4]
        print(f"s: {s}")
        numbs = s.split(" " * 100)
        print(f"numbs: {numbs}")
        s = numbs[0]
        if s == "0":
            return [""]
        numbs = numbs[1:]
        print(f"numbs: {numbs}")
        lst = []
        if s == "":
            return [""]

        i = 0
        final_list = []
        curr = ""
        for i in range(len(numbs)):
            numb = int(numbs[i])
            print(numb)
            final_list.append(s[:numb])
            s = s[numb:]

        return final_list





