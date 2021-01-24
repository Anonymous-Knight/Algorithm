# 给定一个数组，将所有的0移动到数组的末尾，同时保持非零元素的相对顺序
# 不能拷贝额外数组，尽量减少操作次数

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        j = 0
        for i, num in enumerate(nums[::-1]):  # 注意0的相对顺序，从后开始排
            if num == 0:  # 找到0元素
                k = length - i - 1  # 从后遍历的i不再是原数组索引，得到原数组索引k
                while k < length - j - 1:  # 移动到数组末尾
                    temp = nums[k]
                    nums[k] = nums[k + 1]
                    nums[k + 1] = temp
                    k += 1
                j += 1  # 数组末尾的已移动0的数量

# 稍微想复杂了，最简单的方法是去除所有0元素，然后在数组末尾补齐
# 正统一点的方法是双指针，j遍历数组，i统计非零数组
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
# 有意思的是从相反的角度，移动非零元素，思考会简单很多
