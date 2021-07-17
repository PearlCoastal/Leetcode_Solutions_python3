class Solution:
    def breakfastNumber(self, staple: [int], drinks: [int], x: int) -> int:

        ans = 0
        staple.sort()
        drinks.sort()
        ans = 0
        for i in range(len(staple)):
            drink_need = x - staple[i]
            left, right = 0, len(drinks) - 1
            while left <= right:   
                mid = (left + right) // 2
                if drinks[mid] == drink_need:
                    ans += 1
                elif drinks[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
        return ans

staple = [10,20,5]
drinks = [5,5,2]
x = 15

ob = Solution()
ans = ob.breakfastNumber(staple, drinks, x)
ans