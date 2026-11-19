class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = (l + r) // 2
        prev = []
        needed = 0

        while(l < r):

            for i in piles:
                if i > k:
                    if (i % k == 0):
                        needed += i // k
                    else:
                        needed += (i//k) + 1
                elif i <= k:
                    needed += 1
            # 15 > 9, every higher k will give higher number so r = k
            if needed > h:
                l = k + 1
            elif needed <= h:
                r = k
                prev.append(k)

            k = (l + r) // 2
            needed = 0


        return l
            
                
                


         #[1,4,3,2] h =6 we know h >= len(piles) max(piles)
         #k=1 , h =  good
         # while loop until h = 0, with in it a forloop to eat bananas and checl for k,
         # case i > k or i < k
         # if i > k, we subtract h by 1 until  i <= 0 per our rate
         # if i <= k, we subtract 1 and move on
         # increment k by 1 each faliure

         
        