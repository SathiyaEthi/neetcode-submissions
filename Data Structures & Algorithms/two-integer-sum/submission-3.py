class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_values={}
        for index,value in enumerate(nums):
            to_find=target-value
            if to_find in new_values:
             return[new_values[to_find],index]
            new_values[value]=index