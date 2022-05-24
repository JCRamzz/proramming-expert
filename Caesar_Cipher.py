def caesar_cipher(string, offset):
    encodedString = ''
    for letter in string:
        newOffset = ord(letter) - offset
        if newOffset < ord('a'):
            newOffset = (ord(letter) + 26) - offset
        encodedString += chr(newOffset)
    print(type(encodedString))

    return encodedString
print(caesar_cipher('ab', 2))