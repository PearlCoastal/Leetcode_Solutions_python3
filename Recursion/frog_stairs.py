

class Solution():
    def frog_stairs(self, stairs: int) -> int:
        
        if stairs == 1: return 1
        if stairs == 2: return 2
        
        return self.frog_stairs(stairs - 1) + self.frog_stairs(stairs - 2)

stairs = 10
ob = Solution()
ans = ob.frog_stairs(stairs)

ans

'''
1.  题目：  小青蛙一次 跳一级台阶 或 两级台阶 。求 全部跳法。

2.  递归出口：  只有一级台阶的情况， return 1 or 没有台阶的情况， return 0

3.  递归出口为什么没有length == 2时， return 2呢， 小青蛙也可以一次跳两级。
        
        因为这里求的是跳法，而当有两级台阶的时候，跳法有两种，并不可以算作是递归出口

4.  规律：  台阶跳法：  
                    1.  跳一级台阶：    剩下n-1级台阶   共f(n-1)种跳法
                    2.  跳两级台阶：    剩下n-2级台阶   共f(n-2)种跳法
            
    函数的等价关系式:
                    跳法总数：  跳一级台阶 + 跳两级台阶总数之和

                    f(n) = f(n-1) + f(n-2)

'''