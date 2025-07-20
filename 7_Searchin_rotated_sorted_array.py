#LC 33. Search in Rotated Sorted Array
#Where the pivot come that part is unsorted. Like left or right.

def search(arr,tar):
	st, end = 0,len(arr)-1
	while st <= end:
		mid = st + (end-st)//2
		if arr[mid] == tar:
			return mid
		if arr[st] <= arr[mid]:
			if arr[st] <= tar <= arr[mid]:
				end = mid - 1
			else:
				st = mid + 1
		else:
			if arr[mid] <= tar <= arr[end]:
				st = mid + 1
			else:
				end =mid - 1
	return -1
l = [3,1]
ans = search(l,1)
print(ans)