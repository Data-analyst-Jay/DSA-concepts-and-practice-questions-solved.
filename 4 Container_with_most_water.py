#BRUT FORCE 
def max_water(sizes):
	max_capacity = 0
	for i in range(len(sizes)):
		for j in range(i+1,len(sizes)):
			width = j-i
			height = min(sizes[i], sizes[j])
			area = height * width
			max_capacity = max(max_capacity, area)
	print(f'maximum capacity is {max_capacity}')

s = [1,8,6,2,5,4,8,3,7]
# m = max_water(s)

#MORE OPTIMISED (2 pointer approach)
def max_water_opt(sizes):
	max_capacity = 0
	l = 0
	r = len(sizes)-1
	while l<r:
		width = r-l
		height = min(sizes[l], sizes[r])
		ans = height * width
		max_capacity = max(max_capacity, ans)
		if sizes[l]<sizes[r]:
			l+=1
		else:
			r-=1
	print(max_capacity)

max_water_opt(s)