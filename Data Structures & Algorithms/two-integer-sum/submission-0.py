class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums
        for i in range(len(arr)):
            key = arr[i]
            # traverse after leaving the key
            for j in range(i + 1, len(arr)):
                internal_element = arr[j]
                if key + internal_element == target:
                    return [i, j]
        return []

        