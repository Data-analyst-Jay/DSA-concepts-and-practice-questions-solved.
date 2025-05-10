def isvalid(arr,b,s,max_allowedpages):
	stu, pages = 1,0
	for i in range(len(arr)):
		if arr[i] > max_allowedpages:
			return False
		if pages + arr[i] <= max_allowedpages:
			pages += arr[i]
		else:
			stu += 1
			pages = arr[i]
	if stu > s:
		return False
	else:
		return True	

def painter_partition(arr,b,s):
	if s>b:
		return -1
	st, end = 1, sum(arr)-1
	while st<=end:
		mid = st + (end-st)//2
		if isvalid(arr,b,s,mid) == True:
			ans = mid
			end = mid-1
		else:
			st = mid+1	
	return ans

l = [40,30,10,20]
time = painter_partition(l,4,2)
print(f'the minimum time to paint all the boards is {time} units')