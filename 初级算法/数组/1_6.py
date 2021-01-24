# 给定两个数组，计算它们的交集
# 如果给定数组已排序，该如何优化？ --> 双指针，两个数组遍历一次就好
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cup = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    cup.append(nums1[i])
                    nums2.pop(j)  # 防止后续轮重复计算
                    break  # 防止当前轮重复计算
        return cup

# 更好的方法仍是哈希表，遍历nums1统计对应数字出现的次数，遍历nums2统计可重复的次数
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        cup = []
        for n in nums1:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] = 1
        for n in nums2:
            if n in dictionary:
                if dictionary[n] > 0:
                    dictionary[n] -= 1
                    cup.append(n)
        return cup