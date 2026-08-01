class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)
        left = 0
        for n in numbers:
            right = left + 1
            if target - numbers[left] in nums:
                while right < len(numbers):
                    if numbers[left] + numbers[right] == target:
                        return [left + 1, right + 1]
                    right += 1
            left += 1

