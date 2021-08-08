
class Solution:
    def sortArray(self, nums: [int]) -> [int]:

        def partition(left, right):
            pivot = nums[left]

            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        def quickSort(left, right):
            if left >= right:
                return
            pivot = partition(left, right)

            quickSort(left, pivot - 1)
            quickSort(pivot + 1, right)

        quickSort(0, len(nums) - 1)
        return nums


'''
# 比较好理解的交换
def quick_sort_by_shift_left(arr, low, high):
    # 选取最后一个元素作为标志位key，然后将小于key的值前移，最后将标志位放到中间
    if low >= high:
        return
    i = low
    for j in range(low, high):
        if arr[j] <= arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    quick_sort_by_shift_left(arr, low, i - 1)
    quick_sort_by_shift_left(arr, i + 1, high)

'''

nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
nums = [5, 2, 3, 1]
nums = [5, 1, 1, 2, 0, 0]
nums = [10, 9, 8, 7, 6, 5, 3, 4, 2, 1]

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

