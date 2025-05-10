# def prime(n):
#     is_prime = [True for _ in range(n)]
#     for i in range(2,n):
#         if is_prime[i]:
#             pass
#         for j in range(i+1,n,i*2):
#             is_prime[j] = False        
#     for i in is_prime:
#         if i == True:
#             print(i+1) 

# prime(10)

def reverse(n):
    if n==0:
        return 0     
    print(n)
    return reverse(n-1)

reverse(10)    