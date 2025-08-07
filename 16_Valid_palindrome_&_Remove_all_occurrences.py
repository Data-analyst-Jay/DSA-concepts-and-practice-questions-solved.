def valid_pal(str):
    st, end = 0, len(str)-1
    while st < end:
        if str[st].isalnum() == False:
            st+=1
            continue
        if str[end].isalnum() == False:
            end-=1
            continue 
        if str[st].lower() != str[end].lower():
            return 'not a valid palindrome'
        st+=1
        end-=1
    return 'valid palindrome'    

s = 'Ac3?e3c&a'
ans = valid_pal(s)
print(ans)

def remove_occu(s,part):
    while s.find(part.lower()) != -1:
        i = s.find(part.lower())
        s = s[:i] + s[i+len(part):]
    print(s)

remove_occu('daabcbaabcbc', 'abc')
