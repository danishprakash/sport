def twoSum(nums, target):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] in mydict:
            return [mydict[nums[i]], i]
        else:
            mydict[target-nums[i]] = i
    
nums = [int(x) for x in input().split()]
target = int(input())
print(twoSum(nums, target))

