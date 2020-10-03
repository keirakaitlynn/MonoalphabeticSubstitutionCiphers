from random import random, randint
import re

import FRQdict

# keira: ATTRIBUTES: ---------------------------------------------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
keyDRAFT = list(alphabet)  # a mutable list of chars
possibleKeys = {}

# Single Letter Frequencies
expFreqsIncludingSpace = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881,
                          0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490,
                          0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563,
                          0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692,
                          0.0145984, 0.0007836, 0.1918182]


# keira: METHODS: ------------------------------------------------------------------------------------------------------------------
# kkkkk: Convert a listOfChars to a String.
def chars2String(listOfChars):
    str = ""
    for char in listOfChars:
        str += char
    return str


# kkkkk: Returns a string of the given word's WordPattern. ## THIS FUNCTION IS NOT MINE & IS USED FOR SCORING
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


# kkkkk: Returns number of recognizable words in given string  ## THIS FUNCTION IS NOT MINE & IS USED FOR SCORING
def getScore(text):
    copyText = text
    upString = copyText.upper()
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
    #text.lower()
    return chiSquaredScore


# kkkkk: encryption algorithm
def encrypt(message, key):
    CIPHER_text = ""
    for i in message:
        if i in alphabet:
            CIPHER_text += alphabet[key.index(i)]
    return CIPHER_text


# kkkkk: decryption algorithm (SUBSTITUTION)
def decryptSUB(CIPHER_text, key):
    PLAIN_text = ""
    for i in CIPHER_text:
        PLAIN_text += key[alphabet.index(i)]
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


# Substitution Cipher
def option1PARTA(CIPHER_text, key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel):
    determineVowelsAndConsonants(CIPHER_text, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel)
    replaceWithVowelsOrConsonants(CIPHER_text, key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel)
    sandwichMethod(CIPHER_text, key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel)
    replaceRemainingLetters(key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel)
    return key

def getKeyWithMaxScore(CIPHER_text, key):
    # A. Try shifting (Test 25 diff. possible keys).
    bestKeySHIFTINT = 0
    bestScoreSHIFT = 0
    for i in range(1, 26):
        bestScoreSHIFT = getScore(decryptSHIFT(CIPHER_text, bestKeySHIFTINT))
        currScore = getScore(decryptSHIFT(CIPHER_text, i))
        if currScore < bestScoreSHIFT:
            bestKeySHIFTINT = i
    bestKeySHIFT = decryptSHIFT(alphabet, bestKeySHIFTINT) # only found by shifting
    bestScoreSHIFT = getScore(decryptSHIFT(CIPHER_text, bestKeySHIFTINT))

    # B. Try substituting.
    # key_MAX = chars2String(key)
    # text_MAX = decryptSUB(CIPHER_text, key_MAX)
    # score_MAX = getScore(text_MAX)
    # possibleKeys[key_MAX] = score_MAX

    # option 1...
    # reinitialize keyDRAFT
    # keyDRAFT = list(alphabet)  # abcdefgh..
    # reinitialize vowels
    # reinitialize consonants
    # shuffle vowels,
    # shuffle consonants
    # replaceWithVowelsOrConsonants(CIPHER_text) --- changes keyDRAFT

    # option 2... if time, try to incorporate above by swapping whatever letter is a vowel w/ vowel or viceversa for consonants (use isVowel) rather than random indices
    # hill climbing
    MAX = 10000
    numOfIterations = 0
    score_MAX = 50
    score_CURR = 0
    while numOfIterations < MAX:
        key_CURR = list(bestKeySHIFT)
        i = randint(0, 25) % 26
        j = randint(0, 25) % 26
        key_CURR[i], key_CURR[j] = key_CURR[j], key_CURR[i]
        text_CURR = decryptSUB(CIPHER_text, chars2String(key_CURR))  # replace with option 1/ replacewithvc()
        score_CURR = getScore(text_CURR)
        if score_CURR < score_MAX:
            score_MAX = score_CURR
            key_MAX = key_CURR
            possibleKeys[chars2String(key_MAX)] = score_CURR
            numOfIterations = 0
        else:
            numOfIterations += 1

    if score_MAX < bestScoreSHIFT:
        return chars2String(key_MAX)
    else:
        return bestKeySHIFT


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
def determineVowelsAndConsonants(CIPHER_text, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel):
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
def replaceWithVowelsOrConsonants(CIPHER_text, key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel):
    # kkkkk: loop thru each entry in isVowel ( most -> least )
    for letter in isVowel:

        # kkkkk: If letter is a vowel...
        if isVowel[letter]:
            # kkkkk: -> Replace w/ the next most common VOWEL in commonLetters
            nextVowel = vowels.pop()  # removes "e" from vowels

            # print(letter + " -> " + nextVowel)

            commonLetters.remove(nextVowel)  # (remove "e" from commonLetters too.)
            swapLetters(key, letter, nextVowel)

            # key_RESULT = chars2String(key)
            # print("Key AFTER:  " + key_RESULT)
            # print("Key BEFORE: " + alphabet)

# TODO: PART 3: Replace letters before & after VOWELs (letters where isVowel[letter] == True)
#  w/ next common CONSONANT in commonLetters
def sandwichMethod(CIPHER_text, key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel):
    for letter in range(1, len(CIPHER_text)-1):
        # kkkkk: if program thinks this letter isVowel...
        if CIPHER_text[letter] in isVowel and isVowel[CIPHER_text[letter]]:
            letterOnLEFT = CIPHER_text[letter-1]
            letterOnRIGHT = CIPHER_text[letter+1]
            # kkkkk: and program thinks letters on both sides of this letter are CONSONANTs...
            if letterOnLEFT in isVowel and not isVowel[letterOnLEFT] and letterOnRIGHT in isVowel and not isVowel[letterOnRIGHT]:
                # kkkkk: Replace letterOnLeft w/ next common CONSONANT in commonLetters
                commonConsonant = consonants.pop()
                # print(letterOnLEFT + " -> " + commonConsonant)
                commonLetters.remove(commonConsonant)
                swapLetters(key, letterOnLEFT, commonConsonant) # swap letterOnLeft of vowel w/ a consonant
                isVowel[letterOnLEFT] = False # add to isVowel, mark as CONSONANT

                # key_RESULT = chars2String(key)
                # print("Key AFTER:  " + key_RESULT)
                # print("Key BEFORE: " + alphabet)
                # kkkkk: if letterOn left != letterOnRight, then also swap letterOnRight of vowel w/ next common CONSONANT in commonLetters
                if letterOnLEFT != letterOnRIGHT:
                    nextCommonConsonant = consonants.pop()
                    # print(letterOnRIGHT + " -> " + nextCommonConsonant)
                    commonLetters.remove(nextCommonConsonant)
                    swapLetters(key, CIPHER_text[letter+1], nextCommonConsonant)
                    isVowel[letterOnRIGHT] = False  # add to isVowel, mark as CONSONANT

                    # key_RESULT = chars2String(key)
                    # print("Key AFTER:  " + key_RESULT)
                    # print("Key BEFORE: " + alphabet)
    return key

# TODO: PART 4: Replace remaining letters w/ remaining commonLetters. (not in isVowel)
def replaceRemainingLetters(key, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel):
    FRQdictM2L = FRQdict.getSortedDict()
    maxFRQ = FRQdict.getValue(FRQdict.getKeyWithMaxFRQ())

    for entry in FRQdictM2L:
        if entry[0] not in isVowel and len(entry[0]) == 1:
            nextCommonLetter = commonLetters.pop()
            # print(entry[0] + " -> " + nextCommonLetter)
            swapLetters(key, entry[0], nextCommonLetter)

            # key_RESULT = chars2String(key)
            # print("Key AFTER:  " + key_RESULT)
            # print("Key BEFORE: " + alphabet)

    return key

# kkkkk: Swap 2 elem's given an array.
def swapPositions(array, elem1, elem2):
    a, b = array.index(elem1), array.index(elem2)
    array[b], array[a] = array[a], array[b]

# kkkkk: Swap 2 letters in Key to be used by Substitution Cipher.
def swapLetters(thisKey, letterFromCipherText, commonLetter):
    a, b = thisKey.index(letterFromCipherText), thisKey.index(commonLetter)
    thisKey[b], thisKey[a] = thisKey[a], thisKey[b]

# kkkkk: Swap each of the letters of twoLetterCOMBO
#   w/ each of the letters of commonTwoLetterCOMBO
#   in Key to be used by Substitution Cipher.
def swapTwoLetterCOMBOs(thisKey, twoLetterCOMBO, commonTwoLetterCOMBO):
    swapLetters(thisKey, twoLetterCOMBO[0], commonTwoLetterCOMBO[0])
    swapLetters(thisKey, twoLetterCOMBO[1], commonTwoLetterCOMBO[1])

# kkkkk: Swap each of the letters of threeLetterCOMBO
#   w/ each of the letters of commonThreeLetterCOMBO
#   in Key to be used by Substitution Cipher.
def swapThreeLetterCOMBOs(thisKey, threeLetterCOMBO, commonThreeLetterCOMBO):
    swapLetters(thisKey, threeLetterCOMBO[0], commonThreeLetterCOMBO[0])
    swapLetters(thisKey, threeLetterCOMBO[1], commonThreeLetterCOMBO[1])
    swapLetters(thisKey, threeLetterCOMBO[2], commonThreeLetterCOMBO[2])

# kkkkk: Swap each of the letters of fourLetterCOMBO
#   w/ each of the letters of commonFourLetterCOMBO
#   in Key to be used by Substitution Cipher.
def swapFourLetterCOMBOs(thisKey, fourLetterCOMBO, commonFourLetterCOMBO):
    swapLetters(thisKey, fourLetterCOMBO[0], commonFourLetterCOMBO[0])
    swapLetters(thisKey, fourLetterCOMBO[1], commonFourLetterCOMBO[1])
    swapLetters(thisKey, fourLetterCOMBO[2], commonFourLetterCOMBO[2])
    swapLetters(thisKey, fourLetterCOMBO[3], commonFourLetterCOMBO[3])

def getRandomKey():
    randomKey = list(alphabet)
    LIMIT = randint(100, 1000)
    count = 0
    while count < LIMIT:
        i, j = randint(0, 25) % 26, randint(0, 25) % 26
        randomKey[i], randomKey[j] = randomKey[j], randomKey[i]
        count += 1
    return randomKey


# keira: MAIN PROGRAM: ------------------------------------------------------------
def main():
    # 2. Display Menu.
    option = True
    while option:
        print("""
            1. Decrypt (w/ Brute Force, Substitution)
            2. Encrypt & Decrypt (w/ Key)
            3. Exit/Quit
        """)
        # 3. Prompt User for Option.
        option = input("Select an option: ")
        if option == "1":  # ----------------------------------------------
            FRQdict.clearDict()
            # 1. Prompt User for CIPHER_text
            userinput = input("Enter a message: ")
            CIPHER_text = userinput.replace(" ", "")
            createFRQdict(CIPHER_text)
            print("\nDecrypt (w/ Brute Force, Substitution):")

            ## reinit variables whenever this is called (since these are modified throughout)
            # DONT USE: #commonLetters = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
            commonLetters = ["a", "e", "i", "o", "n", "s", "l", "r", "t", "h", "d", "c", "u", "m", "f", "p", "g", "w",
                             "y", "b",
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
            isVowel = {}

            # FRQdict.toString()
            # FRQdict.toStringDL()
            # enter = input("Enter to continue...")
            # print("")
            # option3(CIPHER_text)
            # replaceFourLetterCOMBOs(CIPHER_text)
            # replaceOneLetterCOMBOs(CIPHER_text)
            key = option1PARTA(CIPHER_text, keyDRAFT, commonLetters, vowels, consonants, commonFourLetterCOMBOs, isVowel)
            keyWithMaxScore = getKeyWithMaxScore(CIPHER_text, key)
            print("BEST KEY: " + keyWithMaxScore)
            print(decryptSUB(CIPHER_text, keyWithMaxScore))
        elif option == "2":  # ----------------------------------------------
            print("\nPART 2: Encrypt & Decrypt (w/ Key):")
            text1 = " He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you ."
            text1 = re.sub(r'\W+', '', text1)
            text1 = text1.lower()
            text2 = " There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here , it will 1 instantly disappear and be replaced by something even more bizarre and inexplicable . There is another theory which states that this has already happened ."
            text2 = re.sub(r'\W+', '', text2)
            text2 = text2.lower()
            text3 = " Whenever I find myself growing grim about the mouth ; whenever it is a damp , drizzly November in my soul ; whenever I find myself involuntarily pausing before coffin warehouses , and bringing up the rear of every funeral I meet ; and especially whenever my hypos get such an upper hand of me , that it requires a strong moral principle to prevent me from deliberately stepping into the street , and methodically knocking people ’ s hats off - then , I account it high time to get to sea as soon as I can ."
            text3 = re.sub(r'\W+', '', text3)
            text3 = text3.lower()
            PLAIN_text = [text1, text2, text3]

            for text in PLAIN_text:
                print("")
                randomKey = getRandomKey()
                print("ENCRYPTION KEY: " + chars2String(randomKey))
                textENCRYPTED = encrypt(text, randomKey)
                print("PLAIN_text:  " + text)
                print("encrypt():   " + textENCRYPTED)
                print("decrypt():   " + decryptSUB(textENCRYPTED, randomKey))

        elif option == "3":  # ----------------------------------------------
            print("\nGoodbye!")
            option = False
        elif option != "":  # -----------------------------------------------
            print("\n Not Valid Choice Try again")


# end of main() ------------------------------------------------------------

if __name__ == "__main__":
    main();


#
# commonLetters = ["a", "e", "i", "o", "n", "s", "l", "r", "t", "h", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
# vowels = ["a", "e", "i", "o", "u"]
# consonants = ["l", "s", "t", "r", "n", "p", "c", "f", "g", "m", "d", "z", "b"]
#
#
# # PART 1 -
# def determineVowelsAndConsonants():
#   isVowel = {}
#   for each entry in FRQDict:
#     if entry is one of the top 3 most FRQ letter & is not in a doubleLetterCOMBO:
#       add entry to isVowel, set to TRUE # then consonant
#     elif entry is 1 letter & (FRQ > avgFRQ) & is in a doubleLetterCOMBO:
#       add entry to isVowel, set to TRUE # then consonant
#     elif entry is 2 letters & is a doubleLetterCOMBO:
#       add entry to isVowel, set to FALSE # then vowel
#   return isVowel
#
# # PART 2 - replace after detVC && BEFORE sandwich method
# def replaceWithVowelsOrConsonants(CIPHER_text, isVowel):
#   ## replace letters in isVowel{} depending on whether value is TRUE/FALSE
#   ## with mostCommonVOWEL or mostCommonCONSONANT (key.swap(letter, mostCommonVC))
#   for each letter in isVowel:
#     if isVowel[letter]:
#       replace letter w/ mostCommonVOWEL # pop letter from vowels, remove from CLs
#     else:
#       replace letter w/ mostCommonCONSONANT # pop letter from consonant, remove from CLs
#   # AFTER: ^^ letters in key are swapped accordingly
#
# # PART 3 - sandwich method: | consonant, vowel, consonant |
# def sandwichMethod(CIPHER_text, isVowel):
#   ## LOOP THRU CIPHER_text
#   for letter in range(1, len(CIPHER_text)-1):
#     if isVowel[CIPHER_text[letter]]:
#       ## replace letters around vowels w/ remaining consonants
#       ## replace letters around a vowel w/ most common consonant
#       commonCONSONANT = consonants.pop()
#       swap(CIPHER_text[letter-1], commonCONSONANT) ## edit key
#       commonLetters.remove(commonCONSONANT)
#       if CIPHER_text[letter-1] != CIPHER_text[letter+1]:
#         nextCommonCONSONANT = consonants.pop()
#         swap(CIPHER_text[letter+1], nextCommonCONSONANT) ## edit key
#         commonLetters.remove(nextCommonCONSONANT)
#
# # PART 4 - save key_DRAFT & text_RESULT
# key_INITIAL = key_DRAFT
# text_INITIAL = decryptSUB(CIPHER_text, keyDRAFT)
# score_INITIAL = getScore(text_INITIAL)
# possibleKeys[key_INITIAL] = score_INITIAL
# # A. reset key_DRAFT to str(alphabet)
# # B. REDO PART 1 until all combinations of vowels and consonants have been used
# # C. (enter into a set of keys so that no duplicates can be made)
# key_NEW = key_DRAFT
# text_NEW = decryptSUB(CIPHER_text, key_NEW)
# score_NEW = getScore(text_NEW)
# possibleKeys[key_NEW] = score_NEW
# # D. Compare score_NEW to initial score_INITIAL
# # -> determine which key to throw out (or keep in map of keys "possibleKeys"??)
#
# substitutionCipher(key_DRAFT, CIPHER_text):
# # substitute letters in CIPHER_text using key_DRAFT
# return text_RESULT
#
