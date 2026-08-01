class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while r >= l:
            if nums[(r+l)//2] == target:
                return (r+l)//2
            elif nums[(r+l)//2] > target:
                r = (r+l)//2 - 1
            else:
                l = (r+l)//2 + 1
        return -1
            