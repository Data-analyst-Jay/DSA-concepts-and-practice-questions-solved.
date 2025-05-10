# TC : O(2^n)
# SC : O(n)
class Solution:
    def combinationSum(self, arr, tar):
        comb = []
        ans = set()
        self.helper(arr, 0, comb, ans, tar)
        return [list(tup) for tup in ans]
    
    def helper(self,arr,i,comb,ans,tar):
        if tar==0:
            ans.add(tuple(comb.copy()))
            return
        if i == len(arr) or tar < 0:
            return
        
        comb.append(arr[i])        
        self.helper(arr,i+1,comb,ans,tar-arr[i])
        self.helper(arr,i,comb,ans,tar-arr[i])
        comb.pop()
        
        self.helper(arr,i+1,comb,ans,tar)

A = Solution()
result = A.combinationSum([2,3,5],8)
print(result)