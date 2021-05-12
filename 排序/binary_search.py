'''
def Solution():

    def BinarySearch(array: [int], t: int)-> int:
        low = 0
        height = len(array)-1
        while low < height:
            mid = (low+height)/2
            if array[mid] < t:
                low = mid + 1

            elif array[mid] > t:
                height = mid - 1

            else:
                return array[mid]


array = [1,2,3,34,56,57,78,87]
t = 57

ob = Solution()
ans = ob.
'''

def BinarySearch(array: [int], t: int)-> int:

        low = 0
        height = len(array)-1

        while low <= height:

            mid = int((low + height)/2)
            mid
            if array[mid] < t:
                low = mid + 1

            elif array[mid] > t:
                height = mid - 1

            else:
                return array[mid]

# arr = [2, 3, 4, 10, 40]

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 10
  
result = BinarySearch(array, x)
result
