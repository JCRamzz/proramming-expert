def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

        #   return [index, index + 1]


print(twoSum([15, 11, 2, 7], 9))
# 0  1   2   3
