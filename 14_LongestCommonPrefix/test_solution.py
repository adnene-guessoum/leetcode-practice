from solution import *

def test_return_first_letter_each_element():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == ["t", "t", "p"]

