# BINARY EXPONENTIATION (COMPUTE X^n)
# def pow(X,n):
# 	if n<0:
# 		m = 1/X
# 		n = -(n)
# 	else:
# 		m = X	
# 	ans = 1	
# 	while n>0:
# 		if n % 2 == 1:
# 			ans*=m
# 		m*=m
# 		n//=2
# 	return ans

# a = pow(2,-2)
# print(a)

#BUY AND SELL STOCK FOR MAXIMIZE PROFIT
# def buy_sell(arr):
# 	max_prof = 0
# 	best_buy = arr[0]
# 	for i in range(1,len(arr)):
# 		if best_buy >= arr[i]:
# 			best_buy = min(arr[i],best_buy)
# 		else:
# 			max_prof = max(max_prof,arr[i] - best_buy)
# 	return max_prof, arr.index(best_buy)		

# d = [7,1,5,3,6,4]
# p,D = buy_sell(d)
# print(p,'\n',D)