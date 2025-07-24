# Bubble Sort Implementation
# TC: O(n), O(n)

def bubble(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

a = [4,3,1,5,2]
print(bubble(a))