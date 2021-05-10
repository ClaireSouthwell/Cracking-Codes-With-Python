# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

# The encryption/decryption key
key = 22

# Whether the program encrypts or decrypts
mode = 'decrypt' # set to 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Only symbols included in SYMBOLS can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wraparound if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]

    else:
        # Append the unlisted symbol as-is
        translated += symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
