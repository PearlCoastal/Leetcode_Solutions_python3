
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:

        dict = {}

        for index, value in enumerate(nums):

            num_to_find = target - value

            if num_to_find in dict:
                position = dict[num_to_find]
                return [position, index]
            
            dict.setdefault(value)
            dict[value] = index
        
nums = [2,7,1,9]

target = 9

ob = Solution()
ans = ob.twoSum(nums, target)
ans