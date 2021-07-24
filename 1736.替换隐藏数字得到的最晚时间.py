#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i in range(len(time)):
            if time[i] == '?':
                if i == 0 and time[i + 1] < '4':
                    time[i] = '2'
                elif i == 0 and time[i + 1] >= '4':
                    time[i] = '1'
                elif i == 3:
                    time[i] = '5'
                elif i == 1 and time[i - 1] == '2':
                    time[i] = '3'
                else:
                    time[i] = '9'
        return "".join(time)
# @lc code=end

time = "2?:?0"
time = "0?:3?"
time = "1?:22"
time = "?4:03"

ob = Solution()
ans = ob.maximumTime(time)
ans