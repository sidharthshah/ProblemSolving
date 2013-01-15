class Solver3nPlus1:
    def is_even(self, n):
        return n % 2 == 0

    def maxCycle(self, n):
        cycle = 1
        while n != 1:
            if self.is_even(n):
                n = n / 2
            else:
                n = (3 * n) + 1
            cycle += 1
        return cycle

    def maxCycleRange(self, i, j):
        maxCycle = 0
        for x in range(i, j + 1):
            maxCycle = max(maxCycle, self.maxCycle(x))
        return maxCycle

if __name__ == "__main__":
    s = Solver3nPlus1()
    print s.maxCycleRange(1, 10)
    print s.maxCycleRange(100, 200)
    print s.maxCycleRange(201, 210)
    print s.maxCycleRange(900, 1000)

