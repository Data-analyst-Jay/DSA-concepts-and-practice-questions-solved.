def rev_str(string):
    str = string[::-1]
    ans = ''
    i = 0
    while i < len(string):
        str_word = ''
        
        while i < len(string) and str[i] != ' ':
            str_word += str[i]
            i+=1
        word = str_word[::-1]
        
        if len(word) > 0:
            ans += ' ' + word
        i += 1
    return ans[1:]


def reverseWords(str):
    return " ".join(reversed(str.split()))

ans = reverseWords('Jay Gehlot')
print(ans)

# My Way
def rev_str(str):
    i, j = 0, len(str)-1
    while i < j:
        str[i], str[j] = str[j], str[i]
        i += 1
        j -= 1
    return str

print(rev_str(['j', 'a', 'y', 'g', 'e', 'h', 'l', 'o', 't'])) 