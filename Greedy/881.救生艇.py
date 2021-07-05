#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: [int], limit: int) -> int:

        people.sort()
        ans = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1

        return ans




# @lc code=end

people = [3,2,2,1]
limit = 3

# people = [3,5,3,4]
# limit = 5
# people = [1,2]
# limit = 3

# people = [2,4]
# limit = 5

ob = Solution()
ans = ob.numRescueBoats(people, limit)
ans