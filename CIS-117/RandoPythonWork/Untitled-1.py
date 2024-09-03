def twoSum(nums, target):
        for i in range(len(nums)):
            sum = nums[i] + nums[i + 1]
            if sum == target:
                return [nums[i], nums[i+1]]
            
twoSum([1,2,3,4,5,6], 3)