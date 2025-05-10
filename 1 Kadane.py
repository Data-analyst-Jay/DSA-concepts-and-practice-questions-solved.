# def max_subarray(arr):
# 	curr_sum = 0
# 	max_sum = -1
# 	for i in range(len(arr)):
# 		curr_sum+=arr[i]
# 		max_sum = max(curr_sum,max_sum)
# 		if curr_sum<0:
# 			curr_sum = 0
# 	return max_sum		
# L = [-3,-2,-2,-3]
# R = max_subarray(L)
# print(R)
