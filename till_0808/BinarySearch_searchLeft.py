

# @二分法专题讲义，例题
class Solution():
    def binarySearchLeft(self, nums: [int], target: int) -> int:
        # 左右都闭合的区间 [l, r]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                # 收缩右边界
                right = mid - 1;
            # 搜索区间变为 [mid+1, right]
            if nums[mid] < target: left = mid + 1
            # 搜索区间变为 [left, mid - 1]
            if nums[mid] > target: right = mid - 1
        if left >= len(nums) or nums[left] != target: return -1
        return left

nums = [1,3,3,5,6,7]
target = 3

ob = Solution()
ans = ob.binarySearchLeft(nums, target)
ans