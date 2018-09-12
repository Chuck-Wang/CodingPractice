def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    ans = []
    while matrix:
        ans.extend(matrix.pop(0))
        if matrix and len(matrix[0]) != 0:
            for i in range(len(matrix)):
                ans.append(matrix[i].pop(-1))
        if matrix:
            ans.extend(reversed(matrix.pop(-1)))
        if matrix and len(matrix[0]) != 0:
            for i in range(len(matrix) - 1, -1, -1):
                ans.append(matrix[i].pop(0))
    return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print spiralOrder(matrix)