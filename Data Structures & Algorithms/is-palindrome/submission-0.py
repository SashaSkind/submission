class Solution:
    def normalized(self, s: str) -> str:
        s = s.lower()
        s = s.replace(" ", "")
        clean_s = ""
        for char in s:
            if (48 <= ord(char) <= 57) or (97 <= ord(char) <= 122):
                clean_s += char
        return clean_s

    def isPalindrome(self, s: str) -> bool:
        s = self.normalized(s)
        left = 0
        right = len(s) - 1
        same = True
        while right >= left:
            if s[right] != s[left]:
                same = False
                break
            left += 1
            right -= 1
        return same
        