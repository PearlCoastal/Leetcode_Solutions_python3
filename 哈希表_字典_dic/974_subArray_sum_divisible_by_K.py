class Solution:
    def subarraysDivByK(self, A: [int], K: int) -> int:
        record = {0: 1}
        pre, ans = 0, 0

        for i in A:

            pre += i
            modulus = pre % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1

        return ans




A = [4, 5, 0, -2, -3, 1]
# A = [3, 16, 5]
K = 5

ob = Solution()
ans = ob.subarraysDivByK(A, K)

ans

'''
1.  同余定理：
            给定一个正整数m，如果两个整数a和b满足a-b能够被m整除，即(a-b)/m得到一个整数，那么就称整数a与b对模m同余
            4%5 = 4, 
            同理，(14-9)%5 = 0， 此时 4，9，14三者的结果是一样的，在字典中{4：3}

3.  前缀和本身被5整除的情况: total%5 = 0 的结果 {0: 1}

2.  字典 = {前缀和% K：出现次数}

4.  整除:
        (P[j]-P[i])% K = 0 --> P[j]% K == P[i]% K
        代表从i到j的连续子序列对k整除
        -->求前缀和%k == 0的出现次数
        统计P[i]% K出现的次数
    
5.  pre[j] % k == pre[i] % k --> (pre[j] - pre[i]) % k == 0 --> sum(A[i+1:j]) % k == 0

6.  i = -3时, pre = 4, 此时same = 3, i可取4,5,0,sum(A[i+1:j])

    即i=4:[5, 0, -2, -3], i=5:[0, -2, -3], i=0:[-2, -3]

7.  涉及连续子数组问题: 前缀和

8.  涉及统计出现次数: 字典
    因为哈希表可以在O(1)时间内通过key找到value

'''
