class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        for i in range(len(s)):
            if s[i].isalnum():
                l+=s[i].lower()
        if l==l[::-1]:
            return True
        else:
            return False