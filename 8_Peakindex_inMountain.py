#TC= O(logn)
#LC = 852

def peak(arr):
	st, end = 1, len(arr)-2
	while st <= end:
		mid = st + (end-st)//2
		if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
			return arr[mid]
		if arr[mid-1] < arr[mid]:
			st = mid+1
		else:
			end = mid-1

m = [1,2,3,9,4,5,6,1,2]
ans = peak(m)
print(ans)