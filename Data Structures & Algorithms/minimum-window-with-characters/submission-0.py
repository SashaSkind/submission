class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l = 0
        acc_str = ""
        shortest = ""
        t_dict = defaultdict(int)
        for letter in t:
            t_dict[letter] += 1
        num_of_unique = len(t_dict)
        counter = 0

        window = defaultdict(int)

        for r in range(len(s)):
            window[s[r]] += 1
            acc_str += s[r]

            if window[s[r]] == t_dict[s[r]] and t_dict[s[r]] != 0:
                counter += 1
            while counter == num_of_unique:
                if shortest == "" or len(acc_str) <= len(shortest):
                    shortest = acc_str
                window[s[l]] -= 1
                if window[s[l]] < t_dict[s[l]] and t_dict[s[l]] != 0:
                    counter -= 1
                l += 1
                acc_str = s[l:r+1]
        
        return shortest

        