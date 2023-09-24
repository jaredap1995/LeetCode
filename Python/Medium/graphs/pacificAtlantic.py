class solution:
    def pacificAtlantic(self, heights):
        # Define base case
        if not heights:
            return
        
        #create m, n, and result
        m = len(heights)
        n=len(heights[0])
        res = []

        #Create new array for storing the height from which water flows for position in grid
        peaks = [0]*(m*n)

        #define recursive function to find peaks
        def DFS(i,j,ocean, prevHeight):
            peak_index = (i*n)+j
            if peaks[peak_index]==ocean or peaks[peak_index]==3 or heights[i][j] < prevHeight:
                return
            peaks[peak_index] += ocean
            prevHeight = heights[i][j]

            if peaks[peak_index] == 3:
                res.append([i,j])
            if i+1<m:
                DFS(i+1,j,ocean, prevHeight)
            if i > 0:
                DFS(i-1,j,ocean,prevHeight)
            if j+1<n:
                DFS(i,j+1, ocean, prevHeight)
            if j>0:
                DFS(i,j-1,ocean,prevHeight)

        for i in range(m):
            DFS(i,0,1,heights[i][0])
            DFS(i,n-1,2,heights[i][n-1])

        for j in range(n):
            DFS(0,j,1,heights[0][j])
            DFS(m-1, j, 2, heights[m-1][j])

        return res





        #Iterate over Atlantic


        #Iterate over Pacific