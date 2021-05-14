import random
class Solution:

    def quick_sort(self, nums):    
      
        if len(nums) >= 2:

            mid = nums[len(nums)//2]  

            left, right = [], []
            
            nums.remove(mid)

            for num in nums:            
                if num >= mid: right.append(num)

                else: left.append(num)  

            return self.quick_sort(left) + [mid] + self.quick_sort(right)    
        else:        
            return nums
 

nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
nums = [5, 2, 3, 1]
nums = [5, 1, 1, 2, 0, 0]
nums = [10, 9, 8, 7, 6, 5, 3, 4, 2, 1]

ob = Solution()
ans = ob.quick_sort(nums)

ans


'''
1. quick sort: divide and conquer to divide a list into 2 sub-lists

2. In basically, it's more like a divide and conquer method based on bubble sort

3. one of the fastest sort algorithm

        i. in average, O(nlogn), and the constant factor is much smaller than the merge sort whose complexity is stable and equal to O(nlogn)
        
        ii. although worst at O(n2), when the quick sort of sequential numbers

        iii. for most random numbers with weaker sequence, quick is always better than merge sort

4. i represents the location of mid element, start from left-1

'''

