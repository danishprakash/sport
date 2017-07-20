def findMaxConsecutiveOnes(nums):
    prev_max = [0,0]
    count = [0]
    temp = 0
    if len(nums) == 1 and nums[0] == 1:
        return 1
    for i in range(len(nums)):
        print(i)
        if nums[i] == 1:
            count[temp] += 1
        else:
            count.append(0)
            temp += 1
    return(max(count))
nums = [int(x) for x in input().split()]
print(findMaxConsecutiveOnes(nums))
