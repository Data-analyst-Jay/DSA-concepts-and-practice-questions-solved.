def binary_Search(arr,tar):
    st, end = 0, len(arr)-1
    while st <= end:
        mid = st + (end-st)//2
        if arr[mid] == tar:
            return True
        elif arr[mid] > tar:
            end = mid-1
        else:
            st = mid + 1
    return False
