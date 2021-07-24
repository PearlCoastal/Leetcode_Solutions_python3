剑指 Offer 11. 旋转数组的最小数字
====
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
```剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
```
## 思路

双指针， left right

递增排序数组， 找到旋转点。

`mid = (left + right) // 2`

当 `mid > right` 时， 说明 mid 在左排序数组中， 左界右移， `left = mid + 1`。

当 `mid < right` 时， 说明 mid 在右排序数组中， 要找最小的元素， 所以 右界左移。 

但是有可能 mid 就是最小元素， 所以不要移动的太多了， 以防错过正确解。 `right = mid`。

当 `mid == right` 时， 无法判断， 就只能一步一步缩小右边界 `right -= 1`

## 代码
```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
       
        if not numbers:
            return
        
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]
```

## 复杂度分析
- 时间复杂度： O(logn)
- 空间复杂度： O(1)
