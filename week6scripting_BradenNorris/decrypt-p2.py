codedText = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in codedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
print(plainText)
