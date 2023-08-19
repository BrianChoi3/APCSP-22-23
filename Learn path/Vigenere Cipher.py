defKey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
allKeys = []

def GenerateKey(Keyword):
    for i in Keyword:
        key = []
        ind = defKey.index(i)
        for j in range(ind,26):
            key.append(defKey[j])
        for j in range(0,ind):
            key.append(defKey[j])
        allKeys.append(key)
    return allKeys
       
def Encrypt(Keyword,Message):
    allKeys = GenerateKey(Keyword)
    EncryptedMessage = ""
    for i in range(0,len(Message)):
        if Message[i] == " ":
            EncryptedMessage += " "
        else:
            ind = defKey.index(Message[i])
            EncryptedMessage += allKeys[i%len(Keyword)][ind]
    return EncryptedMessage

def Decrypt(Keyword,Message):
    allKeys = GenerateKey(Keyword)
    DecryptedMessage = ""
    for i in range(0,len(Message)):
        if Message[i] == " ":
            DecryptedMessage += " "
        else:
            ind = allKeys[i%len(Keyword)].index(Message[i])
            DecryptedMessage += defKey[ind]
    return DecryptedMessage

def main():
    print("Welcome to Vigenere Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Keyword = input("Enter the keyword: ")
        Message = input("Enter the message: ")
        print("Encrypted message: ",Encrypt(Keyword,Message))
    elif choice == 2:
        Keyword = input("Enter the keyword: ")
        Message = input("Enter the message: ")
        print("Decrypted message: ",Decrypt(Keyword,Message))
    else:
        print("Invalid choice")

main()