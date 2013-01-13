import sys

class MonsterValley2:
    def minimumPrice(self,dread,price):
        ret = sys.maxint
        bitmask = 0
        while bitmask < (1 << len(dread)):
            total = 0
            cost = 0
            can = True
            j = 0
            while j < len(dread):
                if (bitmask & (1 << j)) > 0:
                    total += dread[j]
                    cost += price[j]
                else:
                    if dread[j] > total:
                        can = False
                        break
                j += 1
            if can:
                ret = min(ret, cost)
            bitmask += 1
        return ret


if __name__ == "__main__":
    mv2 = MonsterValley2()
    print mv2.minimumPrice([8, 5, 10], [1, 1, 2])
    print mv2.minimumPrice([1, 2, 4, 1000000000], [1, 1, 1, 2])
    print mv2.minimumPrice([200, 107, 105, 206, 307, 400], [1, 2, 1, 1, 1, 2])
    print mv2.minimumPrice([5216, 12512, 613, 1256, 66, 17202, 30000, 23512, 2125, 33333], [2, 2, 1, 1, 1, 1, 2, 1, 2, 1])
