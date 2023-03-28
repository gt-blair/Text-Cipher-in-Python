encryptionKey = {"a":32,"b":6,"c":15,"d":21,"e":9,"f":36,
        "g":8,"h":126,"i":45,"j":120,"k":210,
        "l":252,"m":165,"n":330,"o":462,"p":495,
        "q":792,"r":924,"s":1287,"t":1716,"u":3003,
        "v":3432,"w":643,"x":105,"y":102,"z":1365," ":"-"
        }

userMessage = input("Write Your Message: ")

#userMessage = "HelloBrother"

messageLower = userMessage.lower()

encryptedMessage = []
encryptedMessage2 = []

encryptPosition = 0
encryptPosition2 = 0

for i in range(len(messageLower)):
    for k in range(len(encryptionKey)):
        cipher  = encryptionKey[messageLower[encryptPosition]]
        #print(cipher)
        encryptedMessage.append(cipher)
        break
    encryptPosition+=1

#print(encryptedMessage)

for i in range(len(encryptedMessage)):
    #stringValue = str(encryptedMessage[position])
    encryptedMessage2.append(str(encryptedMessage[encryptPosition2]))
    encryptPosition2 += 1

print("".join(encryptedMessage2))  

#space

decryptionKey = {32:'a', 6:'b', 15:'c', 21:'d', 9:'e', 36:'f',
                8:'g', 126:'h', 45:'i',120:'j', 210:'k',
                252:'l', 165:'m', 330:'n', 462:'o', 495:'p',
                792:'q',924:'r',1287:'s', 1716:'t', 3003:'u',
                3432:'v', 643:'w', 105:'x', 102:'y', 1365:'z', '-':' '
                }

decryptedMessage = []

decryptPosition = 0

for i in encryptedMessage:
    for k in decryptionKey:
        decipher = decryptionKey[encryptedMessage[decryptPosition]]
        decryptedMessage.append(decipher)
        #print(decipher)
        break
    decryptPosition += 1

#print(decryptedMessage)

print("".join(decryptedMessage))