## function definition
def searchSortedMatrix(matrix, target):
    ## number of rows
    m = len(matrix)
    if m == 0:
        return False
    ## number of columns
    n = len(matrix[0])
    
    ## binary search implementation
    left, right = 0, m*n-1
    while left <= right:
        mid = left + (right - left)//2
        ## extracting the elements from the 2D array
        ## row_number = idx // n
        ## column_number = idx % n
        mid_element = matrix[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False

## Driver code
matrix = [[1,3,5,7], [10,11,16,20],[23,30,34,60]]
target = 11
## function calling
result = searchSortedMatrix(matrix, target)
print(result)