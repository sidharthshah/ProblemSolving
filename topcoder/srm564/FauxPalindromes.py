class FauxPanlindromes:
    def faux(self, word):
        """
        This method applies faux transformation
        """
        result = ""
        prev_char = word[0]
        i = 1
        for current_char in word[1:]:
            i += 1

            #Handle last character
            if i == len(word):
                if prev_char == current_char:
                    result += current_char
                else:
                    result += prev_char + current_char
                continue

            if prev_char == current_char:
                    continue
            else:
                result += prev_char
                prev_char = current_char
        return result

    def classifyIt(self, word):
        """
        This method is used to classify word
        """
        reverse_word = word[::-1]

        if word == reverse_word:
            return "PALINDROME"
        else:
            faux_word = self.faux(word)
            if faux_word == faux_word[::-1]:
                return "FAUX"

        return "NOT EVEN FAUX"

if __name__ == "__main__":
    fp = FauxPanlindromes()
    print fp.classifyIt("ANA")
    print fp.classifyIt("AAAAANNAA")
    print fp.classifyIt("LEGENDARY")
    print fp.classifyIt("XXXYTYYTTYX")
