import math
class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])

        def gridHelper(row, col):
            # set the total and count
            total, count = 0,0

            top = max(0, row-1)
            bottom = min(m, row+2)
            left = max(0, col - 1)
            right = min(n, col+2)

            for r in range(top, bottom):
                for c in range(left, right):
                    total += img[r][c]
                    count += 1

            return total // count
        
        return [[gridHelper(row, col) for row in m] for col in n]