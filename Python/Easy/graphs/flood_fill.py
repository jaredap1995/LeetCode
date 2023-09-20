class Solution:
    def floodFill(image, sr, sc, color):
        m = len(image)
        n = len(image[0])
        start = image[sr][sc]

        def DFSsearch(i,j):
            if i < 0 or j < 0 or i >=m or j >= n or image[i][j] == color :
                return
            
            image[i][j] = color

            if image[i+1][j] == image[i][j]:
                DFSsearch(i+1,j)
            if image[i-1][j] == image[i][j]:
                DFSsearch(i-1,j)
            if image[i][j-1] == image[i][j]:
                DFSsearch(i, j-1)
            if image[i][j+1] == image[i][j]:
                DFSsearch(i, j+1)

        DFSsearch(sr, sc)

        return image
