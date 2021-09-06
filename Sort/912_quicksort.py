
class Solution:
    def sortArray(self, nums: [int]) -> [int]:


        def quickSort(left, right):
            if left >= right:
                return
            i, j = left, right
            while i < j:
                while nums[j] >= nums[left] and i < j:
                    j -= 1
                while nums[i] <= nums[left] and i < j:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            quickSort(left, i - 1)
            quickSort(j + 1, right)

        quickSort(0, len(nums) - 1)
        return nums


nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
nums = [5, 2, 3, 1]
nums = [5, 1, 1, 2, 0, 0]
nums = [10, 8, 6, 7, 3, 5, 4, 2, 9, 1]

ob = Solution()
ans = ob.sortArray(nums)

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

