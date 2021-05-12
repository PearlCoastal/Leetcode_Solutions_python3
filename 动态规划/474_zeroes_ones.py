# for i in range(5):
#     i

# for i, content in enumerate([3,2,1]):

#     i, content

# for content in [1,2,3]:
#     content


class Solution:


    def Bit_count(self, strs : [str]):

        count_bit = []

        for content in strs:
            
            [num_of_0, num_of_1] = [0,0]

            for bit in content:

                if bit == "0": num_of_0 += 1
                else: num_of_1 += 1

            count_bit.append([num_of_0, num_of_1])

        return count_bit 


    def findMaxForm(self, strs: [str], m: int, n: int) -> int:

        length_of_strs = len(strs)

        Bit_count_res = self.Bit_count(strs)

        dp = [[[0]*(n+1) for zeroes in  range(m+1)] for objects in range(length_of_strs+1)]

        for length in range(1,length_of_strs+1):

            for order_of_0 in range(m+1):
                for order_of_1 in range(n+1):

                    left_0 = order_of_0 - Bit_count_res[length-1][0]

                    left_1 = order_of_1 - Bit_count_res[length-1][1]

                    if(left_0 < 0 or left_1 < 0): 
                        dp[length][order_of_0][order_of_1] = dp[length-1][order_of_0][order_of_1]
                    
                    else: 
                        dp[length][order_of_0][order_of_1] = max(dp[length-1][order_of_0][order_of_1], dp[length-1][left_0][left_1]+1)
  
        return dp[-1][-1][-1]
        
# strs = ["10","0001","111001","1","0"]
# m = 3
# n = 4
#ans = 3

# strs = ["1","0"]
# m = 1
# n = 1
#ans = 2

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
#ans = 4

ob = Solution()

ans=ob.findMaxForm(strs,m,n)
ans
