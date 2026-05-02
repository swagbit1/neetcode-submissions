class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
        # Counter runs in O(n), loops through each and keeps count of char