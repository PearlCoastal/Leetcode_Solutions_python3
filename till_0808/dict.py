from collections import defaultdict

class Solution():

    def lambdawhat(self):
        
        '''
        #利用 lambda函数 对列表嵌套字典 中的 value 进行排序

        d = {'lilee':25, 'wangyan':21, 'liqun':32, 'age':19}

        return sorted(d.items(), key= lambda item: item[1])
        '''

        

        #用defaultdict函数 

        s = [('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

        d = defaultdict(list)

        for k, v in s:

            d[k].append(v)

        return sorted(d.items())
        '''

        c2 = defaultdict(lambda: 123)
        c2[12]
        c2['third']
        return c2
'''

        


ob = Solution()
ans = ob.lambdawhat()
ans
        