
class Solution():

    def subsets(self, nums: [int]) -> [[int]]:

        if not nums:
            return []
        
        length = len(nums)
        res = []
        def backtrack(index: int, path: [int]):
            res.append(path)

            for i in range(index, length):
                backtrack(i + 1, path + [nums[i]])

            return res
        backtrack(0, [])
        return res    


nums = [1,2,3]

ob = Solution()
ans = ob.subsets(nums)
ans
