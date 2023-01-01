class Solution():
	def longestCommonPrefix(self, strs: list[str]) -> str:
		first_letters = []
		for elt in strs:
			first_letters.append(elt[0])

		if len(set(first_letters)) == 1:
			return first_letters[0] 
		else:
			return ""
