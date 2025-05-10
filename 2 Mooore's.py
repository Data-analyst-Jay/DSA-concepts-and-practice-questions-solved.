# Brute force
# def find_pair(arr,T):
# 	P = []
# 	for i in arr:
# 		for j in arr:
# 			if (i!=j) and (i and j not in P) and (i+j ==T):
# 				P.append(i)
# 				P.append(j)
# 				print(i ,'and',j)

# L = [1,2,3,4,5]
# find_pair(L,9)

# More optimised
# def find_pair_opt(arr,T):
# 	i, j = 0, len(arr)-1
# 	while i<j:
# 		S = arr[i]+arr[j]
# 		if S == T:
# 			return arr[i], arr[j]
# 		elif S < T:
# 			i+=1
# 		else:
# 			j-=1

# R=find_pair_opt(L,9)
# print(R)

# MOORE'S ALGORITHM
# 1. Brute force
# def moore_brut(arr):
# 	count = [0 for _ in range(len(arr))]
# 	n = len(arr)//2
# 	for i in range(len(arr)):
# 		for j in range(len(arr)):
# 			if i!=j:
# 				if arr[i]==arr[j]:
# 					count[arr[i]]+=1
# 	for i in count:
# 		if i>n:
# 			return count.index(i)
# B = moore_brut(A)
# print(B)

# 2. Optimized 
# def moore_opt(arr):
# 	freq = 1
# 	prev = arr[0]
# 	for i in range(1,len(arr)):
# 		if arr[i] == arr[i-1]:
# 			freq+=1
# 		else:
# 			freq = 1
# 			prev = arr[i]		
# 		if freq==len(arr)//2:
# 		  return prev		
# A = [1,1,2,2,2,2,3,3,3,3,3,3,3,3]		
# B = moore_opt(A)			
# print(B)

# def moore(arr):
# 	freq = 0
# 	prev = 0
# 	for i in range(len(arr)):
# 		if freq == 0:
# 		  prev = arr[i]
# 		if prev == arr[i]:
# 			freq+=1
# 		else:
# 			freq-=1
# 	return prev

# arr = [1,2,5,4,3,4,4,4,4,4]
# ans = moore(arr)
# print(ans)