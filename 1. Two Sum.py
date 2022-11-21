
##def twoSum(nums, target):
##    """
##    :type nums: List[int]
##    :type target: int
##    :rtype: List[int]
##    """
##
##
##    
##    
##    for i in range(len(nums)):
##        for ii in range(i, len(nums)):
##            if i == ii: continue
##            if nums[i] + nums[ii] == target:
##                return [i, ii]
##        
##[2, 6, 7, 9]  t = 13
##
##{ 2 : 0, 6: 1, 7: 2, 9: 3]



def twoSum(nums, target):
    diff = {nums[i] : i for i in range(len(nums))}
    for i in range(len(nums)):
        value = target - nums[i]
        if diff.get(value, False):
            return [i, diff[value]]
    return "dfguck"


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
