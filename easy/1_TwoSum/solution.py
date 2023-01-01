# thoughts

"""
initial idea:
	check difference between each elements and target to see if the result is
	in array.

better idea:
	store difference in dictionary and check if next difference is in the dict
	to go through the list only once. (each input has exactly one solution)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i, v in enumerate(nums) :
            if ((target - v) in two_sum) :
                return [i, two_sum[(target - v)]]
            else :
                two_sum[v] = i
