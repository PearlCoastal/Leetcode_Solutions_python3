nums = [3, 3, 11, 14]
nums_dict = {}
target = 6


def solution():

    for ind, num in enumerate(nums):
        ind, num

        num2find = target - num
        if num2find in nums_dict:
            
            pos = nums_dict[num2find]
            return[pos,ind]
        nums_dict.setdefault(num)
        nums_dict[num] = ind


sum = solution()
sum
