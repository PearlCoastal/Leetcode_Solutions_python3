class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(position: int):
            
            res = ""
            multi_round = 0

            while position < len(s):

                if '0' <= s[position] <= '9':
                    multi_round = multi_round*10 + int(s[position])
                
                elif s[position] == '[':
                    position, tmp = dfs(position + 1)
                    res += multi_round * tmp
                    multi_round = 0
                
                elif s[position] == ']':
                    return position, res
                
                else:
                    res += s[position]
                
                position += 1
            return res
        
        return dfs(0)

s = "3[a]2[bc]"

ob = Solution()
ans = ob.decodeString(s)

ans