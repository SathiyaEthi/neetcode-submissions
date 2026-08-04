class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list=set(nums)
        len_e=len(nums)
        if len_e > len(new_list):
            return True
        else:
            return False