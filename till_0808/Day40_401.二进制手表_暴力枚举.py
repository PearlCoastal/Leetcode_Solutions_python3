#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> [str]:
        ans = []

        def count(n):
            cnt = 0
            while n:
                n &= (n - 1)
                cnt += 1
            return cnt
        
        for i in range(12):
            for j in range(60):
                if count(i) + count(j) == turnedOn:
                    if j < 10:
                        ans.append(str(i) + ":" + "0" + str(j))
                    else:
                        ans.append(str(i) + ":" + str(j))
        
        return ans

# @lc code=end

num = 1

ob = Solution()
ans = ob.readBinaryWatch(num)
ans
