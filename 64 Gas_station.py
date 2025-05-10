def gast(gas, cost):
    curr_gas = 0
    st = 0
    if sum(gas) < sum(cost):
        return -1
    for i in range(len(gas)):
        curr_gas += (gas[i] - cost[i])
        if curr_gas < 0:
            st = i + 1
            curr_gas = 0
    return st

nums = [5,1,2,3,4]
mums = [4,4,1,5,1]

print(gast(nums,mums))