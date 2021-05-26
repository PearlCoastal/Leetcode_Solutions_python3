class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0

        for c in s:

            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0

            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res

            elif c.isnumeric():
                multi = multi * 10 + int(c)            

            else:
                res += c

        return res

# s = "3[a]2[bc]"
s = "3[a2[c]]"

ob = Solution()
ans = ob.decodeString(s)

ans