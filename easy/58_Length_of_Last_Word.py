class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string
        list_of_word = s.split(" ")
        # check valid words
        only_valid_words = [x for x in list_of_word if len(x)>0]
        # return last word lengh
        return len(only_valid_words[-1])