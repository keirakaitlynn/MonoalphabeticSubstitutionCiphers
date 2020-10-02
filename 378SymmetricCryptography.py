import FRQdict

# keira: ATTRIBUTES: ---------------------------------------------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
global keyDRAFT
keyDRAFT = list(alphabet)  # a mutable list of chars
possibleKeys = {}

# DONT USE: #commonLetters = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
commonLetters = ["a", "e", "i", "o", "n", "s", "l", "r", "t", "h", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b",
                 "v", "k", "x", "j", "q", "z"]
commonLetters.reverse()
vowels = ["a", "e", "i", "o", "u"]
vowels.reverse()
consonants = ["l", "s", "t", "r", "n", "p", "c", "f", "g", "m", "d", "z", "b"]
consonants.reverse()
commonFourLetterCOMBOs = ["tion", "atio", "that", "ther", "with", "ment", "ions", "this",
                          "here", "from", "ould", "ting", "hich", "whic", "ctio", "ence",
                          "have", "othe", "ight", "sion", "ever", "ical", "they", "inte",
                          "ough", "ance", "were", "tive", "over", "ding", "pres", "nter",
                          "comp", "able", "heir", "thei", "ally", "ated", "ring", "ture",
                          "cont", "ents", "cons", "rati", "thin", "part", "form", "ning",
                          "ecti", "some"]
# Single Letter Frequencies
expFreqsIncludingSpace = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881,
                          0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490,
                          0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563,
                          0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692,
                          0.0145984, 0.0007836, 0.1918182]
isVowel = {}


# keira: METHODS: ------------------------------------------------------------------------------------------------------------------

# kkkkk: Convert a listOfChars to a String.
def chars2String(listOfChars):
    str = ""
    for char in listOfChars:
        str += char
    return str


# kkkkk: Returns a string of the given word's WordPattern. ## THIS FUNCTION IS NOT MINE & IS JUST USED FOR SCORING
def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


# kkkkk: Returns number of recognizable words in given string  ## THIS FUNCTION IS NOT MINE & IS JUST USED FOR SCORING
def getScore(text):
    upString = text.lower()
    print(upString)
    CHARS_CONSIDERED = 27;
    charCounts = [0] * CHARS_CONSIDERED
    charFreqs = [0] * CHARS_CONSIDERED
    totCount = 0;

    for c in list(upString):
        index = int(ord(c) - ord('A'))
        if (index >= 0 and index < 26):
            charCounts[index] += 1
            totCount += 1
        if (c == ' '):
            charCounts[26] += 1
            totCount += 1
    if totCount == 0:
        totCount += 1

    chiSquaredScore = 0.0
    for i in range(0, CHARS_CONSIDERED):
        charFreqs[i] = float(charCounts[i]) / float(totCount)
        chiSquaredScore += (charFreqs[i] - expFreqsIncludingSpace[i]) * (charFreqs[i] - expFreqsIncludingSpace[i]) / (
        expFreqsIncludingSpace[i])
    return chiSquaredScore


# kkkkk: encryption algorithm
def encrypt(message, key):
    CIPHER_text = ""
    for i in message:
        CIPHER_text += key[alphabet.index(i)]
    return CIPHER_text


# kkkkk: decryption algorithm (SUBSTITUTION)
def decryptSUB(CIPHER_text, key):
    PLAIN_text = ""
    for i in CIPHER_text:
        PLAIN_text += alphabet[key.index(i)]
    return PLAIN_text


# kkkkk: decryption algorithm (SHIFT)
def decryptSHIFT(CIPHER_text, key):
    PLAIN_text = ""
    for char in CIPHER_text:
        if char.islower():
            PLAIN_text += chr((ord(char) - key - ord('a')) % 26 + ord('a'))
        else:
            PLAIN_text += char
    return PLAIN_text


# kkkkk: Shift Cipher (calls decryptSHIFT x26 times)
def option2(CIPHER_text):
    # A. Try shifting (Test 25 diff. possible keys).
    for key in range(1, 26):
        print("Key = " + str(key) + ": " + decryptSHIFT(CIPHER_text, key))


# kkkkk: Tally up the FRQs of 1-, 2-, 3- & 4-Letter COMBOs in CIPHER_text. Store in FRQdict.
def createFRQdict(CIPHER_text):
    # - tally up occurences of 4-Letter COMBOs in CIPHER_text
    FRQdict.fourLetterFRQ(CIPHER_text)
    # - tally up occurences of 3-Letter COMBOs in CIPHER_text
    FRQdict.threeLetterFRQ(CIPHER_text)
    # - tally up occurences of 2-Letter COMBOs in CIPHER_text
    FRQdict.twoLetterFRQ(CIPHER_text)
    # - tally up occurences of 1-Letter COMBOs in CIPHER_text
    FRQdict.oneLetterFRQ(CIPHER_text)


# TODO: PART 1: Determine which of the letters are VOWELs or CONSONANTs
def determineVowelsAndConsonants(CIPHER_text):
    FRQdictM2L = FRQdict.getSortedDict()
    maxFRQ = FRQdict.getValue(FRQdict.getKeyWithMaxFRQ())

    # kkkkk: loop thru each entry in FRQdict ( most -> least )
    for entry in FRQdictM2L:
        # kkkkk: If entry is 1 letter & entry's FRQ == maxFRQ
        # ###& is not in a doubleLetterCOMBO...
        if len(entry[0]) == 1 and FRQdict.getValue(entry[0]) == (maxFRQ): ## and (not FRQdict.isDoubleLetterCOMBO(entry[0])):
            # kkkkk: -> Add entry to isVowel, set to TRUE
            isVowel[entry[0]] = True
        # kkkkk: If entry is 1 letter & (FRQ > avgFRQ) & is NOT in a doubleLetterCOMBO...
        elif len(entry[0]) == 1 and FRQdict.getValue(entry[0]) > (maxFRQ / 2) and (not FRQdict.isDoubleLetterCOMBO(entry[0])):
            isVowel[entry[0]] = True
        # kkkkk: If entry is 1 letter & (FRQ > avgFRQ) & is in a doubleLetterCOMBO...
        elif len(entry[0]) == 1 and FRQdict.getValue(entry[0]) > (maxFRQ / 2) and FRQdict.isDoubleLetterCOMBO(entry[0]):
            # kkkkk: -> Add entry to isVowel, set to FALSE
            isVowel[entry[0]] = False
        # kkkkk: If entry is 2 letters & is a doubleLetterCOMBO...
        elif len(entry[0]) == 1 and FRQdict.isDoubleLetterCOMBO(entry[0]):
            # kkkkk: -> Add entry to isVowel, set to FALSE
            isVowel[entry[0][0]] = False

# TODO: PART 2: Replace letters w/ VOWELs or CONSONANTs
#  (THIS MUST OCCUR AFTER determineVowelsAndConsonants() && BEFORE sandwichMethod()
def replaceWithVowelsOrConsonants(CIPHER_text):
    # kkkkk: loop thru each entry in isVowel ( most -> least )
    for letter in isVowel:

        # kkkkk: If letter is a vowel...
        if isVowel[letter]:
            # kkkkk: -> Replace w/ the next most common VOWEL in commonLetters
            nextVowel = vowels.pop()  # removes "e" from vowels

            print(letter + " -> " + nextVowel)

            commonLetters.remove(nextVowel)  # (remove "e" from commonLetters too.)
            swapLetters(letter, nextVowel)

            key_RESULT = chars2String(keyDRAFT)
            print("Key AFTER:  " + key_RESULT)
            print("Key BEFORE: " + alphabet)

# TODO: PART 3: Replace letters before & after VOWELs (letters where isVowel[letter] == True)
#  w/ next common CONSONANT in commonLetters
def sandwichMethod(CIPHER_text):
    for letter in range(1, len(CIPHER_text)-1):
        # kkkkk: if program thinks this letter isVowel...
        if CIPHER_text[letter] in isVowel and isVowel[CIPHER_text[letter]]:
            letterOnLEFT = CIPHER_text[letter-1]
            letterOnRIGHT = CIPHER_text[letter+1]
            # kkkkk: and program thinks letters on both sides of this letter are CONSONANTs...
            if letterOnLEFT in isVowel and not isVowel[letterOnLEFT] and letterOnRIGHT in isVowel and not isVowel[letterOnRIGHT]:
                # kkkkk: Replace letterOnLeft w/ next common CONSONANT in commonLetters
                commonConsonant = consonants.pop()
                print(letterOnLEFT + " -> " + commonConsonant)
                commonLetters.remove(commonConsonant)
                swapLetters(letterOnLEFT, commonConsonant) # swap letterOnLeft of vowel w/ a consonant
                isVowel[letterOnLEFT] = False # add to isVowel, mark as CONSONANT

                key_RESULT = chars2String(keyDRAFT)
                print("Key AFTER:  " + key_RESULT)
                print("Key BEFORE: " + alphabet)
                # kkkkk: if letterOn left != letterOnRight, then also swap letterOnRight of vowel w/ next common CONSONANT in commonLetters
                if letterOnLEFT != letterOnRIGHT:
                    nextCommonConsonant = consonants.pop()
                    print(letterOnRIGHT + " -> " + nextCommonConsonant)
                    commonLetters.remove(nextCommonConsonant)
                    swapLetters(CIPHER_text[letter+1], nextCommonConsonant)
                    isVowel[letterOnRIGHT] = False  # add to isVowel, mark as CONSONANT

                    key_RESULT = chars2String(keyDRAFT)
                    print("Key AFTER:  " + key_RESULT)
                    print("Key BEFORE: " + alphabet)

# TODO: PART 4: Replace remaining letters w/ remaining commonLetters. (not in isVowel)
def replaceRemainingLetters():
    FRQdictM2L = FRQdict.getSortedDict()
    maxFRQ = FRQdict.getValue(FRQdict.getKeyWithMaxFRQ())

    for entry in FRQdictM2L:
        if entry[0] not in isVowel and len(entry[0]) == 1:
            nextCommonLetter = commonLetters.pop()
            print(entry[0] + " -> " + nextCommonLetter)
            swapLetters(entry[0], nextCommonLetter)

            key_RESULT = chars2String(keyDRAFT)
            print("Key AFTER:  " + key_RESULT)
            print("Key BEFORE: " + alphabet)

# kkkkk: Swap 2 elem's given an array.
def swapPositions(array, elem1, elem2):
    a, b = array.index(elem1), array.index(elem2)
    array[b], array[a] = array[a], array[b]


# kkkkk: Swap 2 letters in Key to be used by Substitution Cipher.
def swapLetters(letterFromCipherText, commonLetter):
    a, b = keyDRAFT.index(letterFromCipherText), keyDRAFT.index(commonLetter)
    keyDRAFT[b], keyDRAFT[a] = keyDRAFT[a], keyDRAFT[b]


# kkkkk: Swap each of the letters of fourLetterCOMBO
#   w/ each of the letters of commonFourLetterCOMBO
#   in Key to be used by Substitution Cipher.
def swapFourLetterCOMBOs(fourLetterCOMBO, commonFourLetterCOMBO):
    swapLetters(fourLetterCOMBO[0], commonFourLetterCOMBO[0])
    swapLetters(fourLetterCOMBO[1], commonFourLetterCOMBO[1])
    swapLetters(fourLetterCOMBO[2], commonFourLetterCOMBO[2])
    swapLetters(fourLetterCOMBO[3], commonFourLetterCOMBO[3])

# Substitution Cipher
def option3(CIPHER_text):
    determineVowelsAndConsonants(CIPHER_text)
    replaceWithVowelsOrConsonants(CIPHER_text)
    sandwichMethod(CIPHER_text)
    replaceRemainingLetters()

    key_INITIAL = keyDRAFT
    text_INITIAL = decryptSUB(CIPHER_text, key_INITIAL)
    score_INITIAL = getScore(text_INITIAL)
    possibleKeys[keyDRAFT] = score_INITIAL

    print(alphabet)
    print(chars2String(key_INITIAL))
    print(text_INITIAL)

    # reinitialize keyDRAFT
    keyDRAFT = list(alphabet) # abcdefgh..
    # reinitialize vowels
    # reinitialize consonants
    # shuffle vowels,
    # shuffle consonants
    # replaceWithVowelsOrConsonants(CIPHER_text) --- changes keyDRAFT


# keira: MAIN PROGRAM: ------------------------------------------------------------
def main():
    # 1. Prompt User for CIPHER_text
    userinput = input("Enter a message: ")
    CIPHER_text = userinput.replace(" ", "")
    createFRQdict(CIPHER_text)
    # CIPHER_text += "!"

    # 2. Display Menu.
    option = True
    while option:
        print("""
            1. Enter a new message.
            2. Decrypt (w/ Brute Force, Shift)
            3. Decrypt (w/ Brute Force, Substitution)
            4. Decrypt (w/ Key)
            5. Encrypt (w/ Key)
            6. Exit/Quit
        """)
        # 3. Prompt User for Option.
        option = input("Select an option: ")
        if option == "1":
            FRQdict.clearDict()
            userinput = input("\nEnter a message: ")
            CIPHER_text = userinput.replace(" ", "")
            createFRQdict(CIPHER_text)
        elif option == "2":  # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Shift):")
            option2(CIPHER_text)
        elif option == "3":  # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Substitution):")
            FRQdict.toString()
            FRQdict.toStringDL()

            print(FRQdict.isDoubleLetterCOMBO("n"))

            enter = input("Enter to continue...")
            print("")
            # print(FRQdict.getFilteredDict(lambda elem : len(elem[0]) == 4))
            # option3(CIPHER_text)
            # replaceFourLetterCOMBOs(CIPHER_text)
            # replaceOneLetterCOMBOs(CIPHER_text)
            option3(CIPHER_text)

            print("whatsinanamearosebyanyothernamewouldsmellassweet")
        elif option == "4":  # ----------------------------------------------
            print("\nDecrypt (w/ Key)")
        elif option == "5":  # ----------------------------------------------
            print("\nEncrypt (w/ Key)")
        elif option == "6":  # ----------------------------------------------
            print("\nGoodbye!")
            option = False
        elif option != "":  # -----------------------------------------------
            print("\n Not Valid Choice Try again")


# end of main() ------------------------------------------------------------

if __name__ == "__main__":
    main();
