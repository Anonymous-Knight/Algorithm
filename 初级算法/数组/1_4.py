# 给定一个整数数组，判断是否存在重复元素

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 快速排序再判断重复，时间复杂度为O(nlogn + n)
        quick_sort(nums, 0, len(nums) - 1)
        val = nums[0]
        for n in nums:
            if n == val:
                return True
            else:
                val = n
        return False

    def quick_sort(nums, left, right):
        if right <= left:
            return nums
        length = right - left + 1
        a = nums[right]  # 确定主元
        j = left  # 维护比主元小的数组边界
        for i in range(left, right):
            if nums[i] < a:
                if i != j:
                    temp =  nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                j += 1
        # 将主元放到合适的位置
        temp = nums[j]
        nums[right] = temp
        nums[j] = nums[right]

        quick_sort(nums, left, j - 1)  # 主元不参与下一轮排序
        quick_sort(nums, j + 1, right)
        return nums
# 排序后判断重复的思路是对的，但不是最简单的
# 使用哈希表判断是最快速方便的