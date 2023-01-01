# thoughts

"""
initial idea:
	Anagram:
	- same number of letters in both strings	
	- same letters used exactly
	
	Idea:
	=> sort the strings -> compare length -> return false if diff -> if same:
	compare letters in sorted string until diff or end of sorted string

	possible improvements:
	=> don't need to sort before length

"""


# solution :

	# initial idea:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) != len(sorted_t):
            return False

        for i, j in enumerate(sorted_s):
            if j != sorted_t[i]:
               return False
		return True

	# -> result accepted: 60ms (beats 70%), 15.2 mb (not good memory usage)
