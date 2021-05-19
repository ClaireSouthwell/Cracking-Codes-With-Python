# For a transposition cipher, the key may be between 2 and half of the
# message length. The longer the message, the longer the possible key.

import math
# Original values from book example: 
#message = 'Common sense is not so common.'
#key = 8

message = input('Please enter some text to be encrypted: ')
while message == '':
    message = input('No thank you. Please enter some text to be encrypted: ')
    
msg = []
for i in range(len(message)):
    msg.append(message[i])
print(msg)

key = int(input(f'Choose a number between 2 and {len(message)//2}: '))

while key < 2 or key > len(message)//2:
    print('Please play by the rules')
    key = int(input(f'Choose a key between 2 and {len(message)//2}: '))

print(f'Encrypting with a key of {key}')

rows = math.ceil(len(message)/key)
result = ''

counter = 0
while counter < len(message):
    for i in range(key):
        #print(f'Column {i}')
        for j in range(rows):
            #print(j * key)
            if i + j*key < len(message):
                #print(msg[i + j*key])

                result += msg[i + j*key]
            counter += 1

print(result)

'''
# How the book handles the program logic:
for column in range(key):
    # 
    currentIndex = column

    while currentIndex < len(message):
        # Place the character at currentIndex in the message at the end
        # of the current "column" in the ciphertext list
        ciphertext[column] += message[currentIndex]

        #Move the current index over
        # 0, 8, 16, 24; 1, 9, 17, 25; 2, 10, 18, 26 etc
        currentIndex += key
return ''.join(ciphertext)
'''
