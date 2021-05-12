class Solution:

    def threeSum(self, nums: [int]) -> [[int]]:
        
        length = len(nums)

        if(not nums or length < 3): return []

        res = []
        nums.sort()

        for i in range(length):

            if(nums[i] > 0): return res

            if(i > 0 and nums[i] == nums[i - 1]): continue

            #👆这个i > 0啊 学问可大了呢， nums=[0, 0, 0]的时候
            #为什么要continue呢， 如果前后两位数一样，答案可能会出现两对重复值

            left, right = i + 1, length - 1
            while(left < right):
                if(nums[i] + nums[left] + nums[right] == 0): 
                    res.append([nums[i], nums[left], nums[right]])
                
                    while(left < right and nums[left] == nums[left + 1]): left = left + 1
                    while(left < right and nums[right] == nums[right - 1]): right = right - 1
                    left = left + 1
                    right = right - 1
                elif(nums[i] + nums[left] + nums[right] < 0): left = left + 1
                else: right = right - 1
        
        return res


    

nums = [-1,0,1,2,-1,-4]

ob = Solution()
ans = ob.threeSum(nums)

ans