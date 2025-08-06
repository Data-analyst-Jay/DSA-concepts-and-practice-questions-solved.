# def valid_pal(str):
#     st, end = 0, len(str)-1
#     while st < end:
#         if str[st].isalnum() == False:
#             st+=1
#             continue
#         if str[end].isalnum() == False:
#             end-=1
#             continue 
#         if str[st].lower() != str[end].lower():
#             return 'not a valid palindrome'
#         st+=1
#         end-=1
#     return 'valid palindrome'    

# s = 'Ac3?e3c&a'
# ans = valid_pal(s)
# print(ans)

def remove_occu(s,part):
    while part in s:
        s = s.replace(part,'')
    return s

str = "ab"
s = remove_occu(str,'ab')
print(s)