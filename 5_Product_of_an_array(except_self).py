#BRUTE_APPROACH
def prod(arr):
	products = [1 for _ in range(len(arr))]
	for i in range(len(arr)):
		for j in range(len(arr)):
			if j!=i:
				products[i]*=arr[j]
	print(products)

L = [1,2,3,4]		
# prod(L)

def prod_opt(arr):
	suffix = 1
	products = [1 for _ in range(len(arr))]
	for i in range(1,len(arr)):
		products[i] = products[i-1]*arr[i-1]
	for i in range(len(arr)-2,-1,-1):
		suffix*=arr[i+1]
		products[i]*=suffix
	print(products)

# prod_opt(L)