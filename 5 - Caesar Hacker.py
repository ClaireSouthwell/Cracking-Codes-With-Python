# Caesar cipher hacker
# https://www.nostarch.com/crackingcodes/ (BSD licensed)

# message = 'qeFIP?eGSeECNNS,'
# Key 34: I love my kitty, 
# message = '5coOMXXcoPSZIWoQI,'
# Key 44: My kitty loves me,
# message = "avnl1olyD4l'ylDohww6DhzDjhuDil,"
# Key 7: Together we're happy as can be
# message = 'z.GM?.cEQc. 70c.7KcKMKHA9AGFK,'
# Key 32: Though my head has suspicions
# message = '?MFYp2pPJJUpZSIJWpRdpMFY,'
# Key 45: That I keep under my hat,
# message = 'ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K'
# Key 11: Of what if I shrank to the size of a rat,
# message = 'Zfbi,!tif!xpvme!qspcbcmz!fbu!nf'
# Key 1: Yeah, she would probably eat me

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    # Reset translated variable to a blank string to clear the previous attempt
    translated = ''

    # The rest of the program is almost the same as the Caesar program
    # Note that it only has to do decryption 

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound
            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            # Append the decrypted symbol:
            translated += SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated += symbol

    # Display every possible decryption using string interpolation/string formatting: 
    print('Key #%s: %s' % (key, translated))

    # String formatting is great becaue you can insert non-string values
    # that are saved as variables, which you can't do with concatenation 


