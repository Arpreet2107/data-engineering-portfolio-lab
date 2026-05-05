arr = [2, 1, 8, 9, 12, 15, 11, 19]
## Random Access 
print(arr[4])
len(arr)
range(len(arr))
## Search for an element "15" and if it's present in an array, return the index of that element
## Suppose the searching element is not present in an array, return -1
## Time complexity : O(n)
## Space complexity: O(1)
## Function definition
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

## Driver code
print(arr = [2, 1, 8, 9, 12, 15, 11, 19])
x = 15
## Function calling
result = linearSearch(arr, x)
print("Searching element is present at the index", result)
## Insert an element 5 at index 2
## list.insert(index, element)
## Time complexity: O(n)
arr.insert(2, 5)
print(arr)
## Remove an element 8 from the array
## list.remove(element)
## Time complexity: O(n)
arr.remove(8)
print(arr)
## Count the frequency of an element present inside the array
arr.count(2)
arr.count(15)
print(arr)
## Delete an element providing the index 
arr.pop(4)
print(arr)
## Sort the array
arr.sort()
print(arr)
## To extract the index of any given element
arr.index(11)
## To extent the orginal array
arr.extend([2, 5, 7, 10])
print(arr)
## To reverse the entire list
arr.reverse()
print(arr)
#Slicing
arr[1:5]     # subarray
arr[:3]      # first 3 elements
arr[3:]      # from index 3 to end
arr[::-1]    # reverse
#min/max/sum
print(min(arr))
print(max(arr))
print(sum(arr))
#List Comprehension
squared = [x*x for x in arr]
even = [x for x in arr if x % 2 == 0] 