# 给定一个n * n 的矩阵表示一个图像，将图像顺时针旋转90度
# 在原地旋转图像，不能使用另外一个矩阵

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 按圈旋转，直到移动回原点
        start_i, start_j = 0
        length = len(matrix)
        i, j = start_i, start_j + 1
        while i != start_i or j != start_j:
            while 
            matrix[i]
