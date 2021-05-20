# Divide the length of the ciphertext by the key (the number of rows)
# Round up to the nearest number: This is the number of columns

# Rows * columns - length(ciphertext) = the number of empty boxes at the end
# Fill in the boxes row by row
# Read the results column by column

import math, pyperclip

def main():

    ciphertext = 'HcbirhdeuousBdiprrtyevdgpnireeriteatoreechadihfpakengebtedihaoa.dattstn'
    key = 9

    plaintext = decryptMessage(key, ciphertext)
    print(plaintext + '|')
    
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    
    cols = math.ceil(len(message) / key)
    rows = key
    empty = rows * cols - len(message)

    plaintext = [''] * cols 

    row = 0
    col = 0
    
    for symbol in message: 
        plaintext[col] += symbol
        col += 1
        # If there are no more columns or we are at a shaded box,
        # go to the next row
        if (col == cols) or (col == cols - 1 and row >= rows - empty):
            col = 0
            row += 1
        #print(plaintext)

    return ''.join(plaintext)

# If file is run instead of imported as a module, call the main() function
if __name__=='__main__':
    main()


# OTher messages
# HcbirhdeuousBdiprrtyevdgpnireeriteatoreechadihfpakngebtedihaoa.dattstn 
