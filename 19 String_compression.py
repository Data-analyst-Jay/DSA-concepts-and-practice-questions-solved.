#LC443
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