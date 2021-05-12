# import sys 

# class solut
# def tencent_04():

#     length = input()

#     l = list(map(int, input().split()))
'''
class Solution:

    def tencent_04(self, l):    
        
        result = 0
        l.sort()
        
        while(l[-1] - l[0]!=0):
            mid = float((l[0]+l[-1])/2)

            left, right = [], []

            for elements in l:        
                if elements > mid: 
                    right.append(elements)
                    result += elements
                else: 
                    left.append(elements)
                    result += elements

            return self.tencent_04(left) + self.tencent_04(right)    

        return result
 

l = [1, 2, 3]

ob = Solution()
ans = ob.tencent_04(l)

ans
'''

import sys
length = input()
l = list(map(int, input().split()))

result = 0
l.sort()

while(l[-1] - l[0]!=0):
    mid = float((l[0]+l[-1])/2)

    left, right = [], []

    for elements in l:
        if elements > mid:
            right.append(elements)
            result += elements

        else:
            left.append(elements)
            result += elements

    return tencent_04(left) + tencent_04(right)    
            
print(result)
    