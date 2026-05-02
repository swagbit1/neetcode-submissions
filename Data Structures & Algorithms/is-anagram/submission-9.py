class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1
            
        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1


        for char in d1:
            if char in d2:
                if d1[char] != d2[char]:
                    return False
            else:
                return False

        return True
            
