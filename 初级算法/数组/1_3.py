# 给定一个数组，将数组中的元素向右移动k个位置，k为非负数；要求使用空间复杂度为O(1)的原地算法

# 直接暴力解法，一个一个元素移位
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(k):
            x = nums[length - 1]
            for j in range(length - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = x
# 疏漏：range用得不够熟，对边界条件有疏忽；时间复杂度过大，有O(kN)
# 进行优化：一次将元素的位置确定，而不是逐一移位，可达到O(N)，每个元素刚好移动一次
# 问题：以为可以完美地进行移位，这是对问题的数学过程分析错误导致：i元素赋值给i+k%n
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0  
        count = 0
        while count != n:
            curr_idx = start  # 从索引curr_idx开始，将它的值赋给索引(curr_idx + k) % n
            curr_val = nums[start]
            while True:
                next_idx = (curr_idx + k) % n
                temp = nums[next_idx]
                nums[next_idx] = curr_val
                curr_val = temp
                curr_idx = next_idx
                count += 1  # 整个数组只需要n次赋值就可以了，所以count==n
                if curr_idx == start:
                    start += 1  # 从start出发又回到了start，如果count小于n则从start+1处继续开始
                    break