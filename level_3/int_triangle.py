def solution(triangle):

    for i,tri in enumerate(triangle):        
        if i ==0:continue
        for j in range(len(tri)):
            if j ==0:
                triangle[i][j] += triangle[i-1][0]
            elif j ==len(tri) -1: 
                triangle[i][j] += triangle[i-1][-1]
            elif triangle[i-1][j-1]> triangle[i-1][j]:
                triangle[i][j] += triangle[i-1][j-1]
            else: triangle[i][j] += triangle[i-1][j]


    return max(triangle[-1])

triangle= [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))