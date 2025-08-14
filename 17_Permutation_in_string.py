# {No. of chr + Freq of chr} in permutations == Constant
def permu_str(str1,str2):
    n = len(str1)
    freq_1 = [0 for _ in range(26)]
    for i in str1:
        freq_1[ord(i)-ord('a')] += 1

    # wind_size = len(str1)
    indx = 0
    for i in range(0+(n-1),len(str2)):
        wind_freq = [0 for _ in range(26)]
        for j in range(indx,i+1):
            wind_freq[ord(str2[j])-ord('a')] += 1
        indx += 1

        if freq_1 == wind_freq:
            return True
    return False

ans = permu_str('a','ab')
print(ans)

# MY WAY

def permutations(s1, s2):
    if len(s1) > len(s2):
        return False
    n = len(s1)
    f1 = [0]*26
    for i in range(len(s1)):
        f1[ord(s1[i])-ord('a')] += 1
    
    for i in range(len(s2)-n+1):
        f2 = [0]*26
        for j in range(i, i+n):
            f2[ord(s2[j])-ord('a')] += 1
        if f1 == f2:
            return True
    return False