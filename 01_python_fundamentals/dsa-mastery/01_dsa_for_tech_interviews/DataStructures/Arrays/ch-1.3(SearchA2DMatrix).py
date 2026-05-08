# 🚀 Search in a Sorted 2D Matrix using Binary Search

# Matrix properties:
# ✅ Each row is sorted
# ✅ First element of next row is greater
#    than last element of previous row

# Example:
# [
#   [1, 3, 5, 7],
#   [10,11,16,20],
#   [23,30,34,60]
# ]

# Entire matrix behaves like:
# [1,3,5,7,10,11,16,20,23,30,34,60]

# So we can apply Binary Search


def searchSortedMatrix(matrix, target):

    # Total rows
    m = len(matrix)

    # If matrix is empty
    if m == 0:
        return False

    # Total columns
    n = len(matrix[0])

    # Binary Search pointers
    left = 0
    right = m * n - 1

    # Binary Search loop
    while left <= right:

        # Middle index
        mid = left + (right - left) // 2

        # Convert 1D index into 2D position
        row = mid // n
        col = mid % n

        # Middle element from matrix
        mid_element = matrix[row][col]

        # Element found
        if target == mid_element:
            return True

        # Search left half
        elif target < mid_element:
            right = mid - 1

        # Search right half
        else:
            left = mid + 1

    # Element not found
    return False


# Driver Code

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

target = 11

result = searchSortedMatrix(matrix, target)

print(result)

# Output:
# True


# 📊 Time Complexity:
# O(log(m*n))

# 📊 Space Complexity:
# O(1)