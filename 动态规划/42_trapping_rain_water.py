
class Solution:
    def trap(self, height: [int]) -> int:
        
        length = len(height)
        stack = []

        drop = 0

        for i in range(length):
            while(stack and height[i] > height[stack[-1]]):
                curr = stack.pop()

                if(not stack): break

                height_of_drop = min(height[i],height[stack[-1]]) - height[curr]
                drop += (i - stack[-1] -1)*height_of_drop

            stack.append(i)

        return drop


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

ob = Solution()
ans = ob.trap(height)

ans