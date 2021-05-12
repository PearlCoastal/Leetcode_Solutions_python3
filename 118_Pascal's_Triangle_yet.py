'''
class Solution:
    def generate(self, numRows: int) -> [[int]]:

        if numRows == 0: return []
        res = [[1]]

        while len(res) < numRows:

            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            
            res.append(newRow)

        return res
'''

class Solution():
    def generate(self, numRows: int) -> [[int]]:

        result = []

        for i in range(numRows):
            row = []
            for j in range(0, i+1):

                if(j == 0 or j == i): row.append(1)

                else:
                    row[j] = result[i-1][j-1] + result[i-1][j]

            result.append(row)

        return result


numRows = 5

ob = Solution()
ans = ob.generate(numRows)

ans

'''
1. append():

            list1 = ['Google', 'Runoob', 'Taobao']
            list1.append('Baidu')
            ['Google', 'Runoob', 'Taobao', 'Baidu']

2. zip():

        >>>a = [1,2,3]
        >>> b = [4,5,6]
        >>> c = [4,5,6,7,8]
        >>> zipped = zip(a,b)     # 返回一个对象
        >>> zipped

        >>> list(zipped)  # list() 转换为列表
        [(1, 4), (2, 5), (3, 6)]

        >>> list(zip(a,c))              # 元素个数与最短的列表一致
        [(1, 4), (2, 5), (3, 6)]
        
        >>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
        >>> list(a1)
        [1, 2, 3]
        >>> list(a2)
        [4, 5, 6]
        >>>

    3. 嵌套链表

        >>>a = ['a', 'b', 'c']
        >>> n = [1, 2, 3]
        >>> x = [a, n]
        >>> x
        [['a', 'b', 'c'], [1, 2, 3]]
        >>> x[0]
        ['a', 'b', 'c']
        >>> x[0][1]
        'b'
'''