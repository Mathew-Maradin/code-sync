class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()

        for num in range(len(nums)):
            if (target - nums[num]) in visited:
                index = nums.index(target - nums[num]) 
                if index != num:
                    return [index, num]
            else:
                visited.add(nums[num])