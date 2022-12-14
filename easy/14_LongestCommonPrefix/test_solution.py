from solution import *

def passed_test_return_first_letter_each_element():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == ["t", "t", "p"]

def passed_test_compare_first_letter_each_element_false():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == False

def passed_test_compare_first_letter_each_element_true():
	sol = Solution()
	assert sol.longestCommonPrefix(["foot", "fall", "forever"]) == True

def passed_test_return_letter_if_true():
	sol = Solution()
	assert sol.longestCommonPrefix(["foot", "fall", "forever"]) == "f"

def passed_test_return_empty_string_if_false():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "table", "pool"]) == ""

def test_output_for_two_letter_prefix():
	sol = Solution()
	assert sol.longestCommonPrefix(["tree", "trunk", "triangle"]) == "tr"



