class Solution:

    def merge_sort(self, nums, l, r):

        if l == r:
            return
            
        mid = (l + r) // 2

        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)

        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: [int]) -> [int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

# nums = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
# nums = [5, 2, 3, 1]
nums = [5, 1, 1, 2, 0, 0]
# nums = [10, 9, 8, 7, 6, 5, 3, 4, 2, 1]

ob = Solution()
ans = ob.sortArray(nums)

ans
