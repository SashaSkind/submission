class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        counter = defaultdict(int)
        result = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            substr_len = r - l + 1 # 2
            most_freq = 0
            for letter in alphabet:
                most_freq = max(counter[letter], most_freq)
                # 1
            while substr_len - most_freq > k and r >= l:
                counter[s[l]] -= 1
                l += 1
                substr_len -= 1
                
            result = max(result, r - l + 1)
        return result






        