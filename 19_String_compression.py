#LC443
# def compress(arr):
#     count = 1
#     str = ''
#     for i in range(len(arr)-1):
#         if arr[i+1] == arr[i]:
#             count += 1
#         else:
#             if count > 1:
#                 str += f'{arr[i]}{count}'
#                 count = 1
#             elif count == 1:
#                 str += f'{arr[i]}'
#     if count > 1:
#         str += f'{arr[-1]}{count}'
#     else:
#         str += arr[-1]
    
#     arr.clear()
#     for i in range(len(str)):
#         arr.append(f'{str[i]}')

#     print(arr)

# L = ['a','a','b','c','c','c']
# compress(L)


# MY WAY

def compress(arr):
    count = 1
    i,j = 0,1
    while i < len(arr) and j < len(arr):
        if arr[j] == arr[i]:
            count += 1
            i += 1
            j += 1
            continue
        elif arr[j] != arr[i]:
            if count == 1:
                i += 1
                j += 1
                continue
            elif 1 < count < 10:
                arr[count-i:i+1] = [f'{count}']
                i = (count - i + 1)
                j = i + 1
                count = 1
                continue
            elif count >= 10:
                arr[count-i:i+2] = [f'{count//10}', f'{count%10}']
                i = count - i + 2
                j = i + 1
                count = 1
                continue
    
    #For handling the last segment
    if 1 < count < 10:
        arr[j-count+1:j] = [f'{count}']
    elif count >= 10:
        arr[j-count+1:j+1] = [f'{count//10}', f'{count%10}']
    
    return len(arr)

L = ['a', 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
print(compress(L))