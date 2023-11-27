from collections import Counter


class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.testCodes = []
        self.outputCodes = []
        self.segmentFrequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        self.translateSegments = {}
        self.translateDigits = {}
        self.normalDigits = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7,
                             'abcdefg': 8, 'abcdfg': 9}

    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                result = [x.strip() for x in line.split('|')]
                tmp_test_codes = result[0].split(" ")
                tmp_output_codes = result[1].split(" ")
                self.testCodes.append(["".join(sorted(x)) for x in tmp_test_codes])
                self.outputCodes.append(["".join(sorted(x)) for x in tmp_output_codes])

    def print(self):
        print("test codes are:", self.testCodes)
        print("output codes are:", self.outputCodes)

    def solvea(self):
        self.print()
        recognizable_digits = 0
        for line in self.outputCodes:
            print("  ", line)
            for digit in line:
                if len(digit) in {2, 4, 7, 3}:
                    recognizable_digits += 1

        return recognizable_digits

    def determine_translation(self, test_code):
        stringone = ""
        stringfour = ""
        stringeight = ""
        count_chars = Counter("".join(test_code))
        print("test set is", test_code)
        print("  and blank segment frequencies are", self.segmentFrequency)
        print("   and blank segment translations are", self.translateSegments)
        for key in self.segmentFrequency.keys():
            freq = count_chars[key]
            # print("  the frequency of", key, "is", freq)
            self.segmentFrequency[key] = freq
            if freq == 9:
                print("  frequency of key", key, "is 9, so it's f")
                self.translateSegments[key] = 'f'
            elif freq == 4:
                print("  frequency of key", key, "is 4, so it's e")
                self.translateSegments[key] = 'e'
            elif freq == 6:
                print("  frequency of key", key, "is 6, so it's b")
                self.translateSegments[key] = 'b'
        print("  and segment frequencies are", self.segmentFrequency)
        print("   and segment translations so far are", self.translateSegments)

        # determine initially known digits
        stringseven = ""
        for digit in test_code:
            # print("  validating length of", digit, "which is", len(digit))
            if len(digit) == 2:
                print("    digit", digit, "is 1")
                self.translateDigits[digit] = 1
                stringone = digit
            elif len(digit) == 3:
                print("    digit", digit, "is 7")
                self.translateDigits[digit] = 7
                stringseven = digit
            elif len(digit) == 4:
                print("    digit", digit, "is 4")
                self.translateDigits[digit] = 4
                stringfour = digit
            elif len(digit) == 7:
                print("    digit", digit, "is 8")
                self.translateDigits[digit] = 8
                stringeight = digit
        print("  digit translation map so far is", self.translateDigits)

        # deduce remaining segments
        myset = set(stringone)
        knownvals = set(self.translateSegments.keys())
        print("  The character not in", stringone, "and", self.translateSegments.keys(), "is", myset - knownvals)
        self.translateSegments[str(next(iter(myset - knownvals)))] = 'c'
        print("   and updated segment translations are", self.translateSegments)
        myset = set(stringfour)
        knownvals = set(self.translateSegments.keys())
        print("  The character not in", stringfour, "and", self.translateSegments.keys(), "is", myset - knownvals)
        self.translateSegments[str(next(iter(myset - knownvals)))] = 'd'
        print("   and updated segment translations are", self.translateSegments)
        myset = set(stringseven)
        knownvals = set(self.translateSegments.keys())
        print("  The character not in", stringseven, "and", self.translateSegments.keys(), "is", myset - knownvals)
        self.translateSegments[str(next(iter(myset - knownvals)))] = 'a'
        print("   and updated segment translations are", self.translateSegments)
        myset = set(stringeight)
        knownvals = set(self.translateSegments.keys())
        print("  The character not in", stringeight, "and", self.translateSegments.keys(), "is", myset - knownvals)
        self.translateSegments[str(next(iter(myset - knownvals)))] = "g"
        print("   and updated segment translations are", self.translateSegments)

        # final deduction of digits
        for digit in test_code:
            digitstring = ''
            if digit in self.translateDigits:
                pass
            else:
                for segment in digit:
                    # print("    concatinating segment", self.translateSegments[segment], "from", segment)
                    digitstring = digitstring + self.translateSegments[segment]
                # sort the digit string:
                digitstring = "".join(sorted(digitstring))
                print("    translated digit", digit, "is", digitstring, "which is digit",
                      self.normalDigits[digitstring])
                self.translateDigits[digit] = self.normalDigits[digitstring]
        print("   and updated digit translations are", self.translateDigits)

    def decode_number(self, output_code):
        result = ''
        for digit in output_code:
            print("  Decoding digit", digit)
            if digit in self.translateDigits:
                print("   digit", digit, "is translatable and is", self.translateDigits[digit])
                result = result + str(self.translateDigits[digit])
            else:
                print("   digit", digit, "does not exist in translation")
        print("result is", result)
        return int(result)

    def reset_translations(self):
        self.segmentFrequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        self.translateSegments = {}
        self.translateDigits = {}

    def solveb(self):
        total = 0
        for i in range(len(self.testCodes)):
            self.reset_translations()
            self.determine_translation(self.testCodes[i])
            total = total + self.decode_number(self.outputCodes[i])
        return total
