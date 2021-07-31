# Page 173 of Cracking Codes with Python says that with a symbol set length of 66,
# there are 4356 (66^2) possible key combinations for the Affine Cipher.
# However, when you eliminate options for Key A that are not relatively prime
# with 66, the number of possible key combinations drops to 1320.

# I wanted to write a script that would test every key combination for the
# given symbol set to see if I could reproduce these numbers.

# I found that 1320 is the number of possible key combinations IF 0 and 1 are
# accepted as possible keys. It was already established that these are not good
# keys, so I eliminated them as well and found the actual number of possible
# key pairs is even smaller: only 4096 combinations (64^2), 1296 of them valid. 

import sys, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
def main(): 
    getAllKeys()


def gcd(a, b):
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def getAllKeys():
    attempts = 0
    findings = 0
    valid_keys = []
    # To include 0 and 1 as key options, remove the start parameter from the ranges 
    for i in range(2, len(SYMBOLS)):
        for j in range(2, len(SYMBOLS)):
            attempts += 1 
            keyA = i
            keyB = j
            if gcd(keyA, len(SYMBOLS)) == 1:
                findings += 1

                valid_keys.append(keyA * len(SYMBOLS) + keyB)
    print("Attempts: " + str(attempts))
    print("Findings: " + str(findings))
    #print(findings == len(valid_keys))

if __name__ == '__main__':
    main() 
            
