from collections import defaultdict 
from heapq import heappush, heappop
class GooseTattarrattatDiv2:
    @classmethod
    def getmin(self, S):
        counts = defaultdict(int)
        for c in S:
            counts[c] += 1
        
        items = []
        if len(counts.keys()) == 1:
            return 0
        
        result = 0
        for k,v in counts.items():
            heappush(items, (v,k))
        
        while len(items) != 1:
            count, item = heappop(items)
            result += count 
        return result

if __name__ == "__main__":
    assert GooseTattarrattatDiv2.getmin('geese') == 2
    assert GooseTattarrattatDiv2.getmin('tattarrattat') == 6
    assert GooseTattarrattatDiv2.getmin('www') == 0
    assert GooseTattarrattatDiv2.getmin('xrepayuyubctwtykrauccnquqfuqvccuaakylwlcjuyhyammag') == 43
    assert GooseTattarrattatDiv2.getmin('topcoder') == 6
    
    
