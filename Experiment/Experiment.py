# {No. of chr + Freq of chr} in permutations == Constant
# def permu_str(str1,str2):
#     n = len(str1)
#     freq_1 = [0 for _ in range(26)]
#     for i in str1:
#         freq_1[ord(i)-ord('a')] += 1

#     # wind_size = len(str1)
#     indx = 0
#     for i in range(0+(n-1),len(str2)):
#         wind_freq = [0 for _ in range(26)]
#         for j in range(indx,i+1):
#             wind_freq[ord(str2[j])-ord('a')] += 1
#         indx += 1

#         if freq_1 == wind_freq:
#             return True
#     return False

def compress(arr):
    count = 1
    l = []
    for i in range(len(arr)-2):
        if arr[i+1] == arr[i]:
            count += 1
        elif arr[i+1] != arr[i] and arr[i+1] != len(arr)-1:
            l.append(f'{arr[i]}{count}')
            count = 1
    arr = l
    print(arr)

# L = ['a','a','b','b','c','c','c']
# compress(L)

def intersection(l,m):
    result = []
    for i in l:
        if i in m:
            result.append(i)
    return result

# a = [1,2,3,4,5]
# b = [1,3,5,7,9]
# print(intersection(a,b))

def SEO(n):
    ans = 0
    is_prime = [True for _ in range(n)]
    for i in range(2,n):
        if is_prime[i]:
            ans+=1
            for j in range(i*2,n,i):
                is_prime[j] = False
    return ans

def noprime(n):
    if n < 2:
        return 0
    is_prime = [True for _ in range(n)]
    

# print(SEO(10))