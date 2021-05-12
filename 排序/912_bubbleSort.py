
class Solution():

    def bubble_sort(self, nums: [int]):

        length = len(nums)

        for i in range(length):

            for j in range(length - i - 1):

                if(nums[j+1] < nums[j]):

                    nums[j], nums[j+1]  =nums[j+1], nums[j]

        return nums


nums = [64, 34, 25, 12, 22, 11, 90]

ob = Solution()
ans = ob.bubble_sort(nums)

ans

'''
1. why j in range(length - i -1) -> last i elements are already in place

2. how bubble sort functions -> compare 2 elements at 1 time, 
                                switch their places when later one is bigger than the one before
                                and the bigger one will float to the top

3. why i in range(length) ->  there are length elements in list so there will be length round of comparison
                                so here you can observe some useless round and need to be improved

4. when bubble sort faces a sequential list the best complexity will be O(n)

5. and the worst will be O(n2)

6. so the average of complexity will be O(n2)
'''