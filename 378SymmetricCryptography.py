import FRQdict
import operator

# ATTRIBUTES: --------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
keyDRAFT = list(alphabet) # a mutable list of chars
#commonLetters = "etaoinsrhldcumfpgwybvkxjqz"
#commonLetters = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
commonLetters = ["a", "e", "i", "o", "n", "s", "l", "r", "t", "h", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]
#commonLetters.reverse()
vowels = "aeiou"
consonants = "lstrnpcfgmdzb"
commonFourLetterCOMBOs = ["tion", "atio", "that", "ther", "with", "ment", "ions", "this",
                          "here", "from", "ould", "ting", "hich", "whic", "ctio", "ence",
                          "have", "othe", "ight", "sion", "ever", "ical", "they", "inte",
                          "ough", "ance", "were", "tive", "over", "ding", "pres", "nter",
                          "comp", "able", "heir", "thei", "ally", "ated", "ring", "ture",
                          "cont", "ents", "cons", "rati", "thin", "part", "form", "ning",
                          "ecti", "some"] #################################
expFreqsIncludingSpace = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881,
                          0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490,
                          0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563,
                          0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692,
                          0.0145984, 0.0007836, 0.1918182] ###### DELETE / REPLACE

# METHODS: ------------------------------------------------------------
# Convert a listOfChars to a String.
def chars2String(listOfChars):
    str = ""
    for char in listOfChars:
        str += char
    return str

# Returns a string of the given word's WordPattern. #################################
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

# Returns number of recognizable words in given string ###### DELETE / REPLACE
def getScore(text):
    upString = text.upper()
    print(upString)
    CHARS_CONSIDERED = 27;
    charCounts = [0] * CHARS_CONSIDERED
    charFreqs = [0] * CHARS_CONSIDERED
    totCount = 0;

    for c in list(upString):
      index = int(ord(c)-ord('A'))
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
      charFreqs[i] = float(charCounts[i])/float(totCount)
      chiSquaredScore += (charFreqs[i]-expFreqsIncludingSpace[i])*(charFreqs[i]-expFreqsIncludingSpace[i])/(expFreqsIncludingSpace[i])
    return chiSquaredScore

def encrypt(message, key):
    CIPHER_text = ""
    for i in message:
        CIPHER_text += key[alphabet.index(i)]
    return CIPHER_text

def decryptSUB(CIPHER_text, key):
    PLAIN_text = ""
    for i in CIPHER_text:
        PLAIN_text += alphabet[key.index(i)]
    return PLAIN_text

def decryptSHIFT(CIPHER_text, key):
    PLAIN_text = ""
    for char in CIPHER_text:
        if char.islower():
            PLAIN_text += chr((ord(char)-key-ord('a'))%26+ord('a'))
        else:
            PLAIN_text += char
    return PLAIN_text

# Shift Cipher (calls decryptSHIFT x26 times)
def option2(CIPHER_text):
    # A. Try shifting (Test 25 diff. possible keys).
    for key in range(1, 26):
        print("Key = " + str(key) + ": " + decryptSHIFT(CIPHER_text, key))

# Substitution Cipher
def option3(CIPHER_text):
    #do something
    return CIPHER_text

# Tally up the FRQs of 1-, 2-, 3- & 4-Letter COMBOs in CIPHER_text. Store in FRQdict.
def createFRQdict(CIPHER_text):
    # - tally up occurences of 4-Letter COMBOs in CIPHER_text
    FRQdict.fourLetterFRQ(CIPHER_text)
    # - tally up occurences of 3-Letter COMBOs in CIPHER_text
    FRQdict.threeLetterFRQ(CIPHER_text)
    # - tally up occurrences of DOUBLE-Letter COMBOs in CIPHER_text ################# COMPLETE
    #FRQdict.doubleLetterFRQ(CIPHER_text)
    # - tally up occurences of 2-Letter COMBOs in CIPHER_text
    FRQdict.twoLetterFRQ(CIPHER_text)
    # - tally up occurences of 1-Letter COMBOs in CIPHER_text
    FRQdict.oneLetterFRQ(CIPHER_text)

# Replace most FRQ letters in the key with commonLetters
def replaceByMaxFRQ(CIPHER_text):
    
    FRQdictM2L = FRQdict.getSortedDict()

    currScore = 0
    maxScore = 0

    commonLettersITERATION = 0
    vowelsINDEX = 0
    consonantsINDEX = 0

    maxFRQ = FRQdict.getValue(FRQdict.getKeyWithMaxFRQ())
    
    # run this algorithm x5 times to determine which time produces the best score
    #for commonLettersITERATION in range(0, 5):
    
    if commonLettersITERATION != 0:
        swapPositions(commonLetters, commonLetters[0], commonLetters[commonLettersITERATION]) # swap firstElem w/ elem @ num of ITERATION
        
    commonLettersINDEX = 0 # reset index to 0 to re-loop thru commonLetters (post-swap-iteration)
    
    # loop thru each entry in FRQdict ( most -> least )
    for entry in FRQdictM2L:
        while len(commonLetters) != 0:
            # If entry is 1 letter & (FRQ > avgFRQ) & is in a doubleLetterCOMBO...
            if len(entry[0]) == 1 and FRQdict.getValue(entry[0]) > (maxFRQ/2) and FRQdict.isDoubleLetterCOMBO(entry[0]):
                # Replace w/ the next most common VOWEL:
                print(entry[0] + " -> " + vowels[vowelsINDEX])
                swapLetters(entry[0], vowels[vowelsINDEX])
                vowelsINDEX += 1
                commonLetters.remove(vowels[vowelsINDEX])
            # If entry is 1 letter...
            elif len(entry[0]) == 1:
                # Replace w/ the next most common letter:
                print(entry[0] + " -> " + commonLetters[commonLettersINDEX])
                swapLetters(entry[0], commonLetters[commonLettersINDEX]) # swap this entry letter w/ a commonLetter at this INDEX
                commonLettersINDEX += 1
                commonLetters.remove(commonLetters[commonLettersINDEX])
            #if len(entry[0]) == 4:
            

    key_RESULT = chars2String(keyDRAFT)
    print("Key BEFORE: " + alphabet)
    print("Key AFTER:  " + key_RESULT)

    print(CIPHER_text)
    print(decryptSUB(CIPHER_text, key_RESULT))
    print("whatsinanamearosebyanyothernamewouldsmellassweet")

def swapPositions(array, elem1, elem2): 
    a, b = array.index(elem1), array.index(elem2)
    array[b], array[a] = array[a], array[b]

# Swap 2 letters in Key to be used by Substitution Cipher.
def swapLetters(letterFromCipherText, commonLetter):
    a, b = keyDRAFT.index(letterFromCipherText), keyDRAFT.index(commonLetter)
    keyDRAFT[b], keyDRAFT[a] = keyDRAFT[a], keyDRAFT[b]
    
# Swap each of the letters of fourLetterCOMBO
#   w/ each of the letters of commonFourLetterCOMBO
#   in Key to be used by Substitution Cipher.
def swapFourLetterCOMBOs(fourLetterCOMBO, commonFourLetterCOMBO):
    swapLetters(fourLetterCOMBO[0], commonFourLetterCOMBO[0])
    swapLetters(fourLetterCOMBO[1], commonFourLetterCOMBO[1])
    swapLetters(fourLetterCOMBO[2], commonFourLetterCOMBO[2])
    swapLetters(fourLetterCOMBO[3], commonFourLetterCOMBO[3])
    

# MAIN PROGRAM: ------------------------------------------------------------
def main():

    # 1. Prompt User for CIPHER_text
    userinput = input("Enter a message: ")
    CIPHER_text = userinput.replace(" ", "")
    createFRQdict(CIPHER_text)
    #CIPHER_text += "!"
    
    # 2. Display Menu.
    option = True
    while option:
        print ("""
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
        elif option == "2": # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Shift):") 
            option2(CIPHER_text)
        elif option == "3": # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Substitution):")
            FRQdict.toString()
            
            FRQdict.toStringDL()
            print(FRQdict.isDoubleLetterCOMBO("n"))
            
            enter = input("Enter to continue...")
            print("")
            #print(FRQdict.getFilteredDict(lambda elem : len(elem[0]) == 4))
            #option3(CIPHER_text)
            #replaceFourLetterCOMBOs(CIPHER_text)
            #replaceOneLetterCOMBOs(CIPHER_text)
            replaceByMaxFRQ(CIPHER_text)
        elif option == "4": # ----------------------------------------------
            print("\nDecrypt (w/ Key)") 
        elif option == "5": # ----------------------------------------------
            print("\nEncrypt (w/ Key)") 
        elif option == "6": # ----------------------------------------------
            print("\nGoodbye!")
            option = False
        elif option != "": # -----------------------------------------------
            print("\n Not Valid Choice Try again")

# end of main() ------------------------------------------------------------

if __name__ == "__main__":
    main();
