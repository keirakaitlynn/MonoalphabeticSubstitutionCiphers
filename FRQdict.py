import operator

FRQdict = {}

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
        # 2. Count # of times this twoLetterCOMBO appears in CIPHER_text
        if twoLetterCOMBO in FRQdict:
            # twoLetterCOMBO exists
            FRQdict[twoLetterCOMBO] += 1
        else:
            # twoLetterCOMBO does not exist
            FRQdict[twoLetterCOMBO] = 1

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
        
# return value of given key in "FRQdict" dict
def getValue(key):
    return FRQdict[key]

## print(FRQdict.getValue(letterWithMaxFRQ)) # prints maxFRQ in FRQdict

# return key in "FRQdict" w/ the max FRQ
def getKeyWithMaxFRQ():
    return max(FRQdict.items(), key=operator.itemgetter(1))[0]

# delete key in "FRQdict" w/ the max FRQ
def delKeyWithMaxFRQ():
    del FRQdict[max(FRQdict.items(), key=operator.itemgetter(1))[0]]

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
