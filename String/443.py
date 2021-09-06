


class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        while r < len(chars):
            t = 1
            while r + 1 < len(chars) and chars[r] == chars[r+1]:
                r += 1
                t += 1
            if t > 1:
                q = [chars[r]] + list(str(t))
                chars[l:l+len(str(t))+1] = q
                l += len(q)
            else:
                chars[l] = chars[r]
                l += 1
            r += 1
        return l

chars = ["a","a","b","b","c","c","c"]

ob = Solution()
ans = ob.compress(chars)
ans