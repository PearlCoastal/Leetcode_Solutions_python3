class Solution:
    def stoneGame(self, piles: [int]) -> bool:

        length = len(piles)

        dp = [[0]* length for i in range(length)]

        for i in range(length):
            dp[i][i] = piles[i]

        for i in range(length-2, -1, -1):
            for j in range(i+1, length, 1):

                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j] - dp[i][j-1])

        if(dp[0][length-1] > 0): return True
        else: return False





piles = [5, 3, 4, 5]

ob =  Solution()
ans = ob.stoneGame(piles)

ans

'''
1. 限制条件：i. 只能取头尾元素
            ii. 数组的长度是偶数；
            iii.   数组的元素之和是奇数，所以没有平局

2. 重复子问题：  相邻两个堆，求石子之差

                1：亚历克斯拿走左边的i, 剩下dp[i+1][j] 就是李能够获取的最大分数, = piles[i] - dp[i+1][j]
                2: 亚历克斯拿走右边的j, 剩下dp[i][j-1] 就是李能够获取的最大分数, = piles[j] - dp[i][j-1]

3. 填表顺序：   保证左边一格和下边一格的值先计算出来, i倒序叠加

'''