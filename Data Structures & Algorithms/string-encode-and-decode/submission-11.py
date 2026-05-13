class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            s += str(len(i)) + "#" + i
        
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            word = s[j+1: length + j + 1]
            strs.append(word)
            i = length + j + 1
        return strs

        




    # for a string we want its len
    # put it in front of string with a delimititer of #
    # and then read that word until that length
    # and slice that string there
    # game is game would be 4#game2#is4#game
    # we need to read the numnber until the delimiter
    #12#gajkgfweijf... not just the first character
