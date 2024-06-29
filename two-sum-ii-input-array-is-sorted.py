# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1 
        while i < j: 
            total = numbers[i] + numbers[j]
            if total == target: 
                return [i+1, j+1] 
            elif total > target: 
                j -= 1 
            else:
                i += 1 
