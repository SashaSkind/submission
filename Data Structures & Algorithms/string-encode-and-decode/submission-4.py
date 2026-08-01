from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        position = 0
        my_str = ""
        my_list = []
        for i, s in enumerate(strs):
            for l in s:
                my_str += l
                position += 1
            my_list.append(position)
        print(my_str)
        best_sep = " "
        
        for i in range(ord(best_sep), ord(best_sep) + len(my_str) + 1):
            if chr(i) not in my_str:
                best_sep = chr(i)
                break
            best_sep = chr(i + 1)
        
        final_str = ""
        for s in strs:
            for l in s:
                final_str += l
            final_str += best_sep

        print(final_str)
        return final_str
                    
    def decode(self, s: str) -> List[str]:
        if s != "":
            delim = s[-1]
        else:
            return []
        final_list = []
        curr = ""
        for c in s:
            if c != delim:
                curr += c
            else:
                final_list.append(curr)
                curr = ""
        return final_list





