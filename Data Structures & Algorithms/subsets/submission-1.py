class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        tmp = []
        def dfs(i=0):
            if i >= length:
                result.append(tmp.copy())
                return
            
            tmp.append(nums[i])
            dfs(i+1)

            tmp.pop()
            dfs(i+1)
        
        dfs()
        return result

            