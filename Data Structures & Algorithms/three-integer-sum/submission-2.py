class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        list_of_sets = []
        my_hash = {}
        for num in nums:
            if num not in my_hash:
                my_hash[num] = 1
            else:
                my_hash[num] += 1

        print("my hash: ", my_hash)

        for i, n in enumerate(nums):
            #print(my_hash)
            copy_hash = my_hash.copy()
            print(i, copy_hash)
            copy_hash[n] -= 1
            new_nums = nums[i + 1:]
            new_set = set(new_nums)
            target = -n
            for l in new_nums:
                copy_hash[l] -= 1
                if target - l in copy_hash:
                    if copy_hash[target - l] > 0:
                        if {n, l, target - l} not in list_of_sets:
                            list_of_sets.append({n, l, target - l})
                            results.append([n, l, target - l])

        return results
