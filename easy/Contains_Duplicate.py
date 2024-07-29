class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev_value = set()
        for num in nums:
            if num in prev_value:
                return True
            prev_value.add(num)    
        return False