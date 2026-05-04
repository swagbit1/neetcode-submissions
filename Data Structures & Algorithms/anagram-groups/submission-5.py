class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we know counter returns # of character in str
        # if one counter == another than anagrams

        # or take an arry with counted letters as keys, store same type in d

        d = {}

        for word in strs:
            key = [0] * 26
            for i in word.lower():
                index = ord(i) - ord('a')
                key[index]+=1

            key = tuple(key)

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        
        return list(d.values())
