# 判断9*9的数独是否有效，规则为：1-9每行每列只能出现一次，在3*3的宫内只能出现一次
# 数独用二维列表表示，空格部分用'.'表示

class Solution:
    def isValidSudoku(self, board):
        row_dict = [{} for i in range(9)]  # 行字典
        col_dict = [{} for i in range(9)]  # 列字典
        box_dict = [{} for i in range(9)]  # 盒字典

        for i in range(9):
            for j in range(9):
                # 根据数值更新字典
                if board[i][j] != '.':
                    val = board[i][j]
                    row_dict[i][val] = row_dict[i].get(val, 0) + 1  # get返回对应值或默认值，很方便
                    col_dict[j][val] = col_dict[j].get(val, 0) + 1
                    box_index = (i // 3) * 3 + j // 3
                    box_dict[box_index][val] = box_dict[box_index].get(val, 0) + 1

                    if row_dict[i][val] > 1 or col_dict[j][val] > 1 or box_dict[box_index][val] > 1:
                        return False
        return True

# 自己思考的方法是三次遍历，无算法技巧
# 判断重复应很自然地想到哈希表的方法，在遍历数组的过程中维护哈希表实现判断重复
# get()方法还有个默认值返回是之前没有注意到的