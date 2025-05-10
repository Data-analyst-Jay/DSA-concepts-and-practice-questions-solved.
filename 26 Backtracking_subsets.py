# If the arr doesn't have duplicate values
def print_subset(arr, ans, i, result):
    if i == len(arr):
        result.append(ans.copy())
        return 
    
    # Include
    ans.append(arr[i])
    print_subset(arr,ans,i+1,result)

    # exclude
    ans.pop()           #Backtracking works here
    print_subset(arr,ans,i+1,result)

    
def main(arr):
    ans = []
    result = []
    print_subset(arr,ans,0, result)
    return result


# If array have duplicate value
def print_subset(L, ans, i, result):
    arr = sorted(L)
    if i == len(arr):
        result.append(ans.copy())
        return 
    
    # Include
    ans.append(arr[i])
    print_subset(arr,ans,i+1,result)

    # exclude
    ans.pop()
    indx = i+1
    while indx < len(arr) and arr[indx] == arr[indx-1]:
        indx += 1
    print_subset(arr,ans,indx,result)

def main(arr):
    ans = []
    result = []
    print_subset(arr,ans,0, result)
    return result

s = [1,2,2]
subsets = main(s)
print(subsets)