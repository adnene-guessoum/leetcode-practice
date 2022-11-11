class Solution():
	def longestCommonPrefix(self, strs: list[str]) -> str:
		first_letters = []
		for elt in strs:
			first_letters.append(elt[0])
		return first_letters
