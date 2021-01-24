# 给定一个由整数组成的非空数组表示的非负整数，在该数的基础上加一

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = len(digits) - 1  # 最后一位
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
                if i < 0:
                    digits = [1] + digits  # 进位
                    return digits
            digits[i] += 1  # 进位
        else:
            digits[-1] += 1
        return digits
    
# 注意边界情况，只有一位数组