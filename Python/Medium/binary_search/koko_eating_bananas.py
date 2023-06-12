"""
Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas 
from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas 
during this hour.

Koko likes to eat slowly but still wants to finish eating 
all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas 
within h hours.
"""
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        if len(piles)==h:
            return max(piles)

    
        min_speed=1
        max_speed=max(piles)
        while min_speed<max_speed:
            mid=(min_speed+max_speed)//2
            hours_for_all_piles=0
            for pile in piles:
                hours_needed=math.ceil(pile/mid)
                hours_for_all_piles+=hours_needed
            
            if hours_for_all_piles>h:
                min_speed=mid+1
            else:
                max_speed=mid
        return min_speed
            




