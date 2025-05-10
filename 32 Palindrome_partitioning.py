def pp(str, partition, ans):
    if len(str) == 0:
        ans.append(partition.copy())
        return ans
    for i in range(1, len(str)):
        part = str[:i+1]
        if part == part[::-1]:
            partition.append(part)
            pp(str[i:], partition, ans)
            partition.remove(part)
    

s = "aab"
a = pp(s, [], [])
print(a)