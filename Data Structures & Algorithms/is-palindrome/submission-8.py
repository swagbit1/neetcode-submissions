class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.lower().split())
 
 
        l = 0
        r = len(s) - 1 
        

        while len(s) > 1 and l < r:

            while not s[l].isalnum() and l < r:
                l += 1

            
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        #racecar l = 0, r = 6, 
        return True

        #""Was it a car or a cat I saw?""
        
