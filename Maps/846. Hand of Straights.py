from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        if len(hand) % groupSize != 0:
            return False
        
        hand_map = Counter(hand)
        
        for i in hand:
            if hand_map[i] == 0:
                continue
            
            for j in range(i, i+groupSize):
                if hand_map[j] == 0:
                    return False
                hand_map[j] -= 1

        return True
