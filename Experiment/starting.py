# def product(arr):
#     product = arr[0]*arr[1]
#     for i in range(2,len(arr)):
#         overall = product*arr[i]
#         product = overall
#     print(overall)

# def min_max_swap(arr):
#     a = min(arr)
#     i = arr.index(max(arr))
#     j = arr.index(min(arr))
#     arr[j] = max(arr)
#     arr[i] = a
#     print(arr)

# n = int(input('Give i : '))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print('\n')    

# n = eval(input('Provide n :'))
# for i in range(n):
#     C = 'a'
#     for i in range(n):
#         print(C,end='  ')
#         C = chr(ord(C)+1)
#     print('\n')

# def series(n):
# 	m = 1	
# 	for i in range(n):
# 		for j in range(n):
# 			print(m, end=' ')
# 			m+=1	
# 		print('\n')		
# series(10)				

# def stars(m):
# 	n = 1
# 	for i in range(m):
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			j+=1
# 		n+=1
# 		print('\n')	
# stars(10)

# def Alpha(m):
# 	n = 'A'
# 	for i in range(m):
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			j+=1
# 		n = chr(ord(n) + 1)
# 		print('\n')	
# Alpha(10)

# def tri(n):
# 	for i in range(n):
# 		m = 1
# 		j = 0
# 		while j<=i:
# 			print(m,end=' ')
# 			j+=1
# 			m+=1
# 		print('\n')	
# tri(5)		

# def stars(m):
# 	n = 1
# 	for i in range(m):
# 		m = 1
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			j+=1
# 		print('\n')
# 		n+=1
# stars(10)

# def stars(m):
# 	for i in range(m):
# 		n = 1
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			n+=1
# 			j+=1
# 		print('\n')
# stars(10)

# def stars(m):
# 	n = 1
# 	a = 2
# 	for i in range(m):
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			n-=1
# 			j+=1
# 		print('\n')
# 		n = a
# 		a+=1
# stars(5)

# def stars(m):
# 	n = 1
# 	for i in range(m):
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			n+=1
# 			j+=1
# 		print('\n')
# stars(5)

# def stars(m):
# 	n = 1
# 	a = 2
# 	for i in range(m):
# 		j = 0
# 		while j<=i:
# 			print(n,end=' ')
# 			n-=1
# 			j+=1
# 		print('\n')
# 		n = a
# 		a+=1
# stars(5)

# def invstar(n):
# 	space = 1
# 	num = 1
# 	for i in range(n):
# 		while space > 0:
# 			print(' ',end='')
# 			space-=1
# 		for j in range(n-i):
# 			print(num,end=' ')	
# 		num+=1
# 		space+=1
# 		print('\n')
# invstar(5)				

# def unique(a,b):
# 	values = []
# 	set1 = set(a)
# 	set2 = set(b)
# 	unique_values = list(set1 & set2)
# 	for i in unique_values:
# 		values.append(i)
# 	print(values)	
# a = [1,2,3]	
# b = [4,5,6]
# unique(a,b)

# def pyr(n):
# 	for i in range(n):
# 		for j in range(n-i-1):
# 			print(' ',end=' ')
# 		for k in range(i+1):
# 			print(k+1,end=' ')
# 		for l in range(i,0,-1):
# 			print(l,end=' ')
# 		print('\n')

# pyr(4)

# def dia(n):
	# for i in range(n):
	# 	for j in range(n-i-1):
	# 		print(' ',end=' ')
	# 	print('*',end=' ')
	# 	if i!=0:
	# 		for j in range(2*i-1):
	# 			print(' ',end=' ')
	# 		print('*')

# 	for i in range(n-1):
# 		for j in range(i+1):
# 			print(' ',end=' ')
# 		print('*',end=' ')
# 		if i!=n-1:
# 			for j in range(2*(n-i)-5):
# 				print(' ',end=' ')
# 		for j in range(i):
# 			print('*')	
# 		print('\n')

# dia(4)
# def butter(n):
# 	for i in range(n):
# 		for j in range(i+1):
# 			print('*',end=' ')
# 		for j in range(2*(n-i-1),0,-1):
# 			print(' ',end=' ')
# 		for j in range(i+1):
# 			print('*',end=' ')
# 		print('\n')
# 	for i in range(n):
# 		for k in range(n-i):
# 			print('*',end=' ')
# 		for k in range(2*i):
# 			print(' ',end=' ')
# 		for k in range(n-i,0,-1):
# 			print('*',end=' ')			
# 		print('\n')		
# butter(10)

# def rev_tri(n):
# 	for i in range(n):
# 		for j in range(i+1,0,-1):
# 			print(j,end=' ')
# 		print('\n')


# rev_tri(5)

# def floyd(n):
# 	num = 1
# 	for i in range(n):
# 		for j in range(i+1):
# 			print(num,end=' ')
# 			num+=1
# 		print('\n')	
# floyd(5)		

# def invtri(n):
# 	for i in range(n):
# 		for j in range(i+1):
# 			print(' ',end='')
# 		for k in range(n-i):
# 			print(i+1,end='')
# 		print('\n')		

# invtri(9)		

# def invpyr(n):
# 	for i in range(n):
# 		for j in range(i+1):
# 			print(' ',end='')
# 		for k in range(n-i):
# 			print(i+1,end=' ')
# 		print('\n')

# invpyr(9)

# def rev_int(n):
# 	a = None
# 	rev_num = 0
# 	while n!=0:
# 		a = n%10
# 		n//=10
# 		rev_num = rev_num*10 + a	
# 	print(rev_num)	
# rev_int(12345)		

def fibo(nth):
    if nth == 0 or nth == 1:
        return nth
    return fibo(nth-2) + fibo(nth-1)

def if_sorted(arr,n):
    if n == 0 or n == 1:
        return True
    return arr[n-1] >= arr[n-2] and if_sorted(arr,n-1)

def binary_search(arr,n,st,end):
    if st <= end:    
        mid = st + (end-st)//2
        if arr[mid] == n:
            return mid
        if n > arr[mid]:
            return binary_search(arr,n,mid+1,end)
        else:
            return binary_search(arr,n,st,mid-1)
    return -1

def print_element(l):
    for i in l:
        for j in i:
            print(j, end = ' ')
        print('\n')

E = []
def insert_element2d(E):
    row = int(input('Enter the number of rows : '))
    col = int(input('Enter the number of column : '))
    for i in range(col):
        n = []
        for j in range(row):
            a = eval(input('Enter the value : '))
            n.append(a)
        E.append(n)
    print(E)


def search_2d(arr,tar):
    for i in arr:
        for j in i:
            if j == tar:
                return (arr.index(i), i.index(j))
    return (-1,-1)

def max_row_sum(arr):
    max_sum = float('-inf')
    for i in arr:
        sum_row = 0
        for j in i:
            sum_row += j
            if sum_row > max_sum:
                max_sum = sum_row
    return max_sum

# def diagonal_sum(M,size):
#     sum = 0
#     for i in range(size):
#         sum += M[i][i]
#         if i != size-i-1:
#             sum += M[i][size-i-1]
#     return sum

def compress(arr):
    count = 1
    str = ''
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            count += 1
        else:
            if count > 1:
                str += f'{arr[i]}{count}'
                count = 1
            elif count == 1:
                str += f'{arr[i]}'
    if count > 1:
        str += f'{arr[-1]}{count}'
    else:
        str += arr[-1]
    
    arr.clear()
    for i in range(len(str)):
        arr.append(f'{str[i]}')

    print(arr)

L = ['a','a','b','c','c','c']
compress(L)