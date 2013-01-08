class FoxAndHandleEasy:
    def isPossible(self, S, T):
        """
        This function is used to check if string can be expanded
        """

        for i in range(len(S)):
            current = S[0:i] + S + S[i:]

            if current == T:
                return "Yes"
        return "No"

if __name__ == "__main__":
    fahe = FoxAndHandleEasy()
    print fahe.isPossible("Ciel", "CieCiell")
    print fahe.isPossible("Ciel", "FoxCiel")
    print fahe.isPossible("FoxCiel", "FoxFoxCielCiel")
