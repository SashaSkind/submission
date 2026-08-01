class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        c = 0
        for n in nums:
            if n == 0:
                c = c + 1
            if n != 0:
                product = product * n
        output = [0] * len(nums)
        if c > 1:
            return output

        if c == 1:
             for i, n in enumerate(nums):
                if n == 0:
                    output[i] = product

        else: 
            for i, n in enumerate(nums):
                if n != 0:
                    output[i] = int(product / n)
                else:
                    output[i] = product
        return output
        