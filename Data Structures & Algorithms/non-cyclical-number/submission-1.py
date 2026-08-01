class Solution:

    def findSum(self, n: int) -> int:
        length = len(str(n))
        sum = 0
        for _ in range(length):
            num = n % 10
            n //= 10
            sum += num ** 2
        return sum


    def isHappy(self, n: int) -> bool:
        results = set()

        r = n
        while True:
            r = self.findSum(r)
            if r  == 1:
                return True
            if r in results:
                return False
            results.add(r)
        
        print(sum)
        return True

        