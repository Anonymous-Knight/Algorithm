# 给定一个排序数组，在原地删除重复出现的元素，并返回移除后数组的长度；不使用额外的数组空间，在原地修改输入数组并在O(1)的额外空间完成

# 排序数组意味着重复元素必定相邻，且只可能在后面，由此想到对每个新元素，遍历其邻近元素
# 即双指针解法，一指针指向新数组元素，一指针遍历旧数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
# 疏漏的地方：没有考虑极限情况：数组长度为0时的逻辑，虽然恰好能用