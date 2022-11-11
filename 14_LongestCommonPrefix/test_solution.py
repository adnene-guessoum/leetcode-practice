from solution import *

def passed_test_return_first_letter_each_element():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == ["t", "t", "p"]


def test_compare_first_letter_each_element_false():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == False

def test_compare_first_letter_each_element_true():
	sol = Solution()
	assert sol.longestCommonPrefix(["foot", "fall", "forever"]) == True

