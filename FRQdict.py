import operator

FRQdict = {}
doubleLetterCOMBOs = {}

# determine how freq. 1 letter appears in given CIPHER_text
def oneLetterFRQ(CIPHER_text):
    for letter in CIPHER_text:
        # 1. Count # of times a letter appears in CIPHER_text.
        if letter in FRQdict:
            # letter exists
            FRQdict[letter] += 1 # this letter appears +1 more time
        else:
            # letter does not exist
            FRQdict[letter] = 1 # this letter appears once

# determine how freq. a 2-letter COMBO appears in given CIPHER_text
def twoLetterFRQ(CIPHER_text):
    for i in range(len(CIPHER_text)-1):
        # determine twoLetterCOMBO
        twoLetterCOMBO = CIPHER_text[i] + CIPHER_text[i+1]
        # 2. If twoLetterCOMBO is a doubleLetterCOMBO, add to doubleLetterCOMBOs{}
        if CIPHER_text[i] == CIPHER_text[i+1] and twoLetterCOMBO in doubleLetterCOMBOs:
            doubleLetterCOMBOs[twoLetterCOMBO] += 1
        elif CIPHER_text[i] == CIPHER_text[i+1] and twoLetterCOMBO not in doubleLetterCOMBOs:
            doubleLetterCOMBOs[twoLetterCOMBO] = 1
        # 3. Count # of times this twoLetterCOMBO appears in CIPHER_text
        if twoLetterCOMBO in FRQdict:
            # twoLetterCOMBO exists
            FRQdict[twoLetterCOMBO] += 1
        else:
            # twoLetterCOMBO does not exist
            FRQdict[twoLetterCOMBO] = 1

### determine how freq. a DOUBLE-letter COMBO appears in given CIPHER_text
##def doubleLetterFRQ(CIPHER_text):
##    for i in range(len(CIPHER_text)-1):
##        # determine doubleLetterCOMBO
##        if CIPHER_text[i] == CIPHER_text[i+1]:
##            doubleLetterCOMBO = CIPHER_text[i] + CIPHER_text[i+1]
##            if doubleLetterCOMBO in FRQdict:
##                FRQdict[doubleLetterCOMBO] += 1
##            else:
##                FRQdict[doubleLetterCOMBO] = 1

# determine how freq. a 3-letter COMBO appears in given CIPHER_text
def threeLetterFRQ(CIPHER_text):
    for i in range(len(CIPHER_text)-2):
        # determine threeLetterCOMBO
        threeLetterCOMBO = CIPHER_text[i] + CIPHER_text[i+1] + CIPHER_text[i+2]
        # 2. Count # of times this threeLetterCOMBO appears in CIPHER_text
        if threeLetterCOMBO in FRQdict:
            # threeLetterCOMBO exists
            FRQdict[threeLetterCOMBO] += 1
        else:
            # threeLetterCOMBO does not exist
            FRQdict[threeLetterCOMBO] = 1

# determine how freq. a 4-letter COMBO appears in given CIPHER_text
def fourLetterFRQ(CIPHER_text):
    for i in range(len(CIPHER_text)-3):
        # determine fourLetterCOMBO
        fourLetterCOMBO = CIPHER_text[i] + CIPHER_text[i+1] + CIPHER_text[i+2] + CIPHER_text[i+3]
        # 2. Count # of times this fourLetterCOMBO appears in CIPHER_text
        if fourLetterCOMBO in FRQdict:
            # fourLetterCOMBO exists
            FRQdict[fourLetterCOMBO] += 1
        else:
            # fourLetterCOMBO does not exist
            FRQdict[fourLetterCOMBO] = 1

# get fourLetterCOMBOs in FRQdict w/ more than given "numOfFRQ"
def getFourLetterCOMBOs(numOfFRQ):
    fourLetterCOMBOs = dict(filter(lambda elem: len(elem[0]) == 4 and elem[1] > numOfFRQ, FRQdict.items()))
    return fourLetterCOMBOs

# get OneLetterCOMBOs in FRQdict w/ more than given "numOfFRQ"
def getOneLetterCOMBOs(numOfFRQ):
    oneLetterCOMBOs = dict(filter(lambda elem: len(elem[0]) == 1 and elem[1] > numOfFRQ, FRQdict.items()))        
    return oneLetterCOMBOs

# get FRQdict sorted by FRQ (most to least)
def getSortedDict():
    FRQdictM2L = sorted(FRQdict.items(), key=lambda x: x[1], reverse=True)
    return FRQdictM2L ###########################

# Determines if given letter(s) is a doubleLetterCOMBO.
def isDoubleLetterCOMBO(letterOrLetters):
  if (len(letterOrLetters) == 1):
    twoLetterCOMBO = letterOrLetters + "" + letterOrLetters
    return twoLetterCOMBO in doubleLetterCOMBOs ###############
  else:
    return letterOrLetters in doubleLetterCOMBOs

# return value of given key in "FRQdict" dict
def getValue(key):
    return FRQdict[key]

# return key in "FRQdict" w/ the max FRQ
def getKeyWithMaxFRQ():
    return max(FRQdict.items(), key=operator.itemgetter(1))[0]

# delete key in "FRQdict" w/ the max FRQ
def delKeyWithMaxFRQ():
    del FRQdict[max(FRQdict.items(), key=operator.itemgetter(1))[0]]

def clearDict():
    FRQdict.clear()

def isEmpty():
    return not bool(FRQdict)

# (NOTE: MUST REPLACE!)
#########

# print dictionary (most - > least)
def toString():
    # dictionary (most - > least)
    FRQdictM2L = sorted(FRQdict.items(), key=lambda x: x[1], reverse=True)
    print("")
    print("FRQdict: -------")
    # for every letter/letterCOMBO tracked
    for i in FRQdictM2L:
        # print the letter/letterCOMBO & their FRQ
        #print(i + str(FRQdictM2L[i]))
        print("key: " + i[0] + ", value: " + str(i[1]))
    print("----------------")
    print("")

# print dictionary (most - > least)
def toStringDL():
    # dictionary (most - > least)
    doubleLetterCOMBOsM2L = sorted(doubleLetterCOMBOs.items(), key=lambda x: x[1], reverse=True)
    print("")
    print("doubleLetterCOMBOs: -------")
    # for every letter/letterCOMBO tracked
    for i in doubleLetterCOMBOsM2L:
        # print the letter/letterCOMBO & their FRQ
        #print(i + str(FRQdictM2L[i]))
        print("key: " + i[0] + ", value: " + str(i[1]))
    print("----------------")
    print("")
