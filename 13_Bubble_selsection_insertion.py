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
# print(bubble(a))

def selection(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

# print(selection(a))

def insertion(arr):
    for i in range(1, len(arr)):
        s = arr[i]
        j = i-1
        while j >= 0 and s < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = s
    return arr

print(insertion(a))