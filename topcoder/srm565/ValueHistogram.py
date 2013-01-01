#Author: Sidharth Shah
#Email: iamsidd [at] gmail [dot][com]
#Solutions to http://community.topcoder.com/stat?c=problem_statement&pm=12275&rd=15187

class ValueHistogram:
    def build(self, values):
        histogram = []
        counts = [0] * (max(values) + 1)
        for eachValue in values:
            counts[eachValue] += 1

        height = max(counts) + 1

        for i in range(height):
            current = []
            for j in range(len(counts)):
                if counts[j] > 0:
                    current.append("X")
                    counts[j] -= 1
                else:
                    current.append(".")
            histogram.append(current)
        histogram.reverse()
        return histogram

if __name__ == "__main__":
    v = ValueHistogram()
    print v.build([2, 3, 5, 5, 5, 2, 0, 8])
    print "\n"
    print v.build([9, 9, 9, 9])
