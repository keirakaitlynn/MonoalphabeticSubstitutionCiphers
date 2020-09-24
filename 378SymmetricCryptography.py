import FRQdict
import operator

# ATTRIBUTES: --------------------------------------------------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
keyDRAFT = list(alphabet) # a mutable list of chars
commonLetters = "etaoinsrhldcumfpgwybvkxjqz"

# METHODS: ------------------------------------------------------------
# Convert a listOfChars to a String.
def chars2String(listOfChars):
    str = ""
    for char in listOfChars:
        str += char
    return str

# Swap 2 letters in Key.
def swap(letterWithMaxFRQ, commonLetter):
    a, b = keyDRAFT.index(letterWithMaxFRQ), keyDRAFT.index(commonLetter)
    keyDRAFT[b], keyDRAFT[a] = keyDRAFT[a], keyDRAFT[b]

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

# A. Tally up the FRQs of 1-, 2-, 3- & 4-Letter COMBOs in CIPHER_text. Store in FRQdict.
def createFRQdict(CIPHER_text):
    # - tally up occurences of 4-Letter COMBOs in CIPHER_text
    FRQdict.fourLetterFRQ(CIPHER_text)
    # - tally up occurences of 3-Letter COMBOs in CIPHER_text
    FRQdict.threeLetterFRQ(CIPHER_text)
    # - tally up occurences of 2-Letter COMBOs in CIPHER_text
    FRQdict.twoLetterFRQ(CIPHER_text)
    # - tally up occurences of 1-Letter COMBOs in CIPHER_text
    FRQdict.oneLetterFRQ(CIPHER_text)
    
    FRQdict.toString() # print contents of FRQdict

def option2(CIPHER_text):
    # A. Try shifting (Test 25 diff. possible keys).
    for key in range(1, 26):
        print("Key = " + str(key) + ": " + decryptSHIFT(CIPHER_text, key))

def option3(CIPHER_text):
    FRQdict.toString() # print contents of FRQdict

    # B. Alter keyDRAFT accordingly. (NOTE: this assumes FRQdict contains single letters ONLY)
    # while letters exists in FRQdict:
    commonLettersCOUNTER = 0
    while not FRQdict.isEmpty(): # (NOTE: this replaces every letter in CIPHER_text w/ a commonLetter)

        # - determine which letter to replace with a common letter CHECK
        letterWithMaxFRQ = FRQdict.getKeyWithMaxFRQ()
        print(letterWithMaxFRQ + " -> " + commonLetters[commonLettersCOUNTER])

        # - swap letterWithMaxFRQ w/ common letter CHECK
        swap(letterWithMaxFRQ, commonLetters[commonLettersCOUNTER])

        # - delete letterWithMaxFRQ from FRQdict (NOTE: this deletes all existing keys in FRQdict)
        FRQdict.delKeyWithMaxFRQ()
        
        # - commonLettersCOUNTER++
        commonLettersCOUNTER += 1

    # C. Finalize key. (Convert listOfChars "keyDRAFT" to str)
    finalKey = chars2String(keyDRAFT)

    print("")
    print("Key BEFORE: " + alphabet)
    print("Key AFTER:  " + finalKey)
    print("commonLetters: " + commonLetters)

    # D. Decrypt CIPHER_text.
    print(decryptSUB(CIPHER_text, finalKey))

# MAIN PROGRAM: ------------------------------------------------------------
def main():

    # 1. Prompt User for CIPHER_text
    userinput = input("Enter a message: ")
    CIPHER_text = userinput.replace(" ", "")
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
            userinput = input("\nEnter a message: ")
            CIPHER_text = userinput.replace(" ", "")
        elif option == "2": # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Shift):") 
            option2(CIPHER_text)
        elif option == "3": # ----------------------------------------------
            print("\nDecrypt (w/ Brute Force, Substitution):")
            createFRQdict(CIPHER_text)
            print("")
            enter = input("Enter to continue...")
            print("")
            testFilter()
            #option3(CIPHER_text)
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
