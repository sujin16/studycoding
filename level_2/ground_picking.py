def solution(land):
    arr=land.pop(0)
    for la in land:
        for i in range(4):
            before =arr[:]
            del before[i]
            la[i]+=max(before)
        arr =la
    return max(arr)
land= 	[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))