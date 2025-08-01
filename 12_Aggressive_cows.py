def possible(l,c,mid):
	L = sorted(l)
	cow, last_position = 1, L[0]
	for i in L:
		if (last_position - i) >= mid:
			cow += 1
			last_position = i
		if cow == c:
			return True
	return False	
def agc(l,s,c):
	if c==1:
		return 0
	st, end = 1, max(l) - min(l)
	while st <= end:
		mid = st + (end-st)//2
		if possible(l,c,mid) == True:
			ans = mid
			end = mid + 1
		else:
			st = mid - 1
	return ans			

a = [1,2,8,4,9]
ans = agc(a,5,3)
print(ans)