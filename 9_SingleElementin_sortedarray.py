def single(arr):
	st, end = 0, len(arr)-1
	if len(arr) == 1:
		return arr[0]
	while st <= end:
		mid =st + (end-st)//2
		if mid == 0 and arr[mid] != arr[mid+1]:
			return arr[mid]
		if mid == len(arr)-1 and arr[mid] != arr[mid-1]:
			return arr[mid]
		if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
			return arr[mid]
		if mid%2 == 0:
			if arr[mid] == arr[mid-1]:
				end = mid-1
			else:
				st = mid + 1
		else:
			if arr[mid] == arr[mid-1]:
				st = mid + 1
			else:
				end = mid - 1				
s = [3,3,7,7,10,11,11]
ans = single(s)
print(ans)