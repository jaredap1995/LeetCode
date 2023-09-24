var floodFill = function(image, sr, sc, color) {

    if (!image || !image.length || image[sr][sc]===color) {return image}

    let m = image.length
    let n = image[0].length
    let val = image[sr][sc]

    var DFS = (i,j) => {
        if (i<0 || j <0 || i>=m || j >=n || val !== image[i][j])  {return}

        image[i][j]=color
        DFS(i+1,j)
        DFS(i-1, j)
        DFS(i,j+1)
        DFS(i,j-1)
    }

    DFS(sr,sc)
    return image
}