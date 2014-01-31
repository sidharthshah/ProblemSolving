class KeyDungeonDiv2:
    @classmethod
    def countDoors(self, doorR, doorG, keys):
        result = 0
        for i in range(len(doorR)):
            wk = keys[2]

            if keys[0] >= doorR[i]:
                rk = doorR[i]
            else:
                rk = keys[0]
                if wk >= (doorR[i] - keys[0]):
                    rk += (doorR[i] - keys[0])
                    wk -= (doorR[i] - keys[0])

            if keys[1] >= doorG[i]:
                gk = doorG[i]
            else:
                gk = keys[1] + wk

            result += 1 if rk >= doorR[i] and gk >= doorG[i] else 0
        return result

if __name__ == "__main__":
    assert KeyDungeonDiv2.countDoors([2, 0, 5, 3], [1, 4, 0, 2],[2, 3, 1]) == 3
    assert KeyDungeonDiv2.countDoors([0, 1, 2, 0], [0, 2, 3, 1],[0, 0, 0]) == 1
    assert KeyDungeonDiv2.countDoors([3, 5, 4, 2, 8], [4, 2, 3, 8, 1],[0, 0, 10]) == 5
    assert KeyDungeonDiv2.countDoors([4, 5, 4, 6, 8], [2, 1, 2, 3, 5],[1, 2, 1]) == 0