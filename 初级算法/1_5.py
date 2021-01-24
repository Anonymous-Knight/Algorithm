# 给定一个非空整数数组，其中某个元素只出现一次，其余元素均出现两次，找出只出现一次的元素

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for n in nums:
            if n in dictionary:
                del dictionary[n]
            else:
                dictionary[n] = 1
        return list(dictionary.keys())[0]

# 对于重复问题，第一个应想到的是哈希表解法
# 这里注意字典的keys()返回不是list类型，需要强制转换