class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        queue = deque()
        
        l = 0
        r = 0

        for r in range(len(nums)):
            while queue and nums[r] >= queue[-1][1]:
                queue.pop()
            queue.append((r, nums[r]))

            if queue[0][0] < l:
                queue.popleft()
            if queue and r >= k - 1:
                l += 1
                maxes.append(queue[0][1])
        return maxes
        

        