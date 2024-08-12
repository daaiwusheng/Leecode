class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filterd = ''.join(filter(str.isalnum, s))
        s_filterd = s_filterd.lower()
        resversed_s = s_filterd[::-1]
        return s_filterd == resversed_s
