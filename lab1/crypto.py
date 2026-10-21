#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.

    Add more implementation details here.
    """
    result = ""
    i=0
    for character in plaintext:
        code = ord(character)
        if code in  range(65, 91):
            code = ((code -65 + 3) % 26 ) + 65
            character = chr(code)
        result += character
        i+=1
    return result
    #raise NotImplementedError  # Your implementation here


def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.
    """
    result = ""
    i=0
    for character in ciphertext:
        code = ord(character)
        if code in  range(65, 91):
            code = ((code - 65 - 3) % 26 ) + 65
            character = chr(code)
        result += character
        i+=1
    return result
    raise NotImplementedError  # Your implementation here


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    result = ""
    i=0
    j=0
    keyword_list = list(keyword)
    for character in plaintext:
        code = ord(character)
        if code in  range(65, 91):
            keyword_code = ord(keyword_list[j])
            code = ((code + keyword_code) % 26 ) + 65
            character = chr(code)
            j = (j+1) % len(keyword)
        result += character
        i+=1
    return result
    #raise NotImplementedError  # Your implementation here


def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    result = ""
    i=0
    j=0
    keyword_list = list(keyword)
    for character in ciphertext:
        code = ord(character)
        if code in  range(65, 91):
            keyword_code = ord(keyword_list[j])
            code = ((code - keyword_code) % 26 ) + 65
            character = chr(code)
            j = (j+1) % len(keyword)
        result += character
        i+=1
    return result
    #raise NotImplementedError  # Your implementation here

#Scytale
def encrypt_scytale(plaintext, circumference):
    result_list = []
    result = ""
    i=0
    plaintext_list = list(plaintext)
    length = len(plaintext)

    while (length % circumference !=0 ):
        plaintext_list.append('x')
        length+=1

    nr_rows = (length // circumference)
    for i in range(0,length):
        result_list.append( plaintext_list[ ((i % nr_rows) * circumference) + (i // nr_rows)] )
    result = "".join(result_list)

    return result

def decrypt_scytale(ciphertext, circumference):
    result_list = []
    result = ""
    i=0
    ciphertext_list = list(ciphertext)
    length = len(ciphertext)

    while (length % circumference !=0 ):
        ciphertext_list.append('x')
        length+=1

    row_len = (length // circumference)
    for i in range(0,length):
        result_list.append( ciphertext_list[ ((i % circumference) * row_len) + (i // circumference)] )
    result = "".join(result_list)
    
    return result


#Railfence
def encrypt_railfence(plaintext, num_rails):
    result_list = []
    result = ""
    i=0
    plaintext_list = list(plaintext)
    length = len(plaintext)
    cycle_len = 2 * num_rails - 2

    for i in range(0, num_rails):
        j=0
        while(True):
            if i == 0:
                if (j) * cycle_len >= length:
                    break
                result_list.append(plaintext_list[(j) * cycle_len])
            elif i == (num_rails-1):
                if i + j * cycle_len >= length:
                    break
                result_list.append(plaintext_list[i + j * cycle_len])
            else:
                if i + j * cycle_len >= length: 
                    break
                result_list.append(plaintext_list[i + j * cycle_len])

                if cycle_len - i - 1 + j * cycle_len >= length:
                                    break
                result_list.append(plaintext_list[cycle_len - i + j * cycle_len])
            j+=1

    result = "".join(result_list)
    return result

def decrypt_railfence(ciphertext, num_rails):

    rail_height_frequency = [0] * num_rails
    current_level = 0
    length = len(ciphertext)
    down = True
    for i in range(length):
        rail_height_frequency[current_level] += 1
        if current_level == 0:
            down = True
        elif current_level == num_rails - 1:
            down = False

        if (down):
            current_level+=1
        else:
            current_level-=1
        

    containers = []
    j=0 
    for frequency in rail_height_frequency:
        chars = list(ciphertext[j : j + frequency])
        containers.append(chars)
        j += frequency
        
    result_list = []
    current_level = 0
    down = True
    
    for i in range(length):
        result_list.append(containers[current_level].pop(0))
        
        if current_level == 0:
            down = True
        elif current_level == num_rails - 1:
            down = False
            
        if down:
            current_level += 1
        else:
            current_level -= 1
            
    return "".join(result_list)

# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

