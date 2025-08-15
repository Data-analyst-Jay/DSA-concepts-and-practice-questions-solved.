# Time complexity = log(m*n)
def search_2d(M,tar):
    st, end = 0, len(M)-1
    while st <= end:
        mid = st + (end-st)//2
        if M[mid][0] <= tar <= M[mid][len(M[mid])-1]:
            row = mid
            break
        elif tar < M[mid][0]:
            end = mid - 1
        else:
            st = mid + 1

    st_r, end_r = 0, len(M[row])-1
    while st_r <= end_r:
        mid_r = st_r + (end_r-st_r)//2
        if tar == M[row][mid_r]:
            return (row,mid_r)
        elif tar < M[row][mid_r]:
            end_r = mid_r - 1
        else:
            st_r = mid_r + 1
    return -1

L = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# ans = search_2d(L,34)
# print(ans)

# Search in a 2D matrix II
# Rows are overlapping in terms of rows
def search_2D2(M,tar):
    st, end = 0, len(M[0])-1
    while end >= 0 and st < len(M):
        if tar == M[st][end]:
            return True
        elif tar < M[st][end]:
            end -= 1
        else:
            st += 1
    return False

ans = search_2D2(L,16)
print(ans)