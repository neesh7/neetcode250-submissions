class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Basically Sets, Can't have Duplicate Elements so converting it uniquely
        non_duplicate = list(set(nums))

        # Now scanning for if any duplicate is present we will see a size difference if not then no     duplicate
        if len(nums) == len(non_duplicate):
            return False
        return True