# crypto.py
# Functions for CS 1 Lab Assignment 4.
#Author: Sarah Korb
#Nov. 9, 2018
#Prof. Cormen: CS1
from random import randint

d = 143335107525767630766681992050243383450593422653797373240583295055192203309151620171296230900825953 #secret key
n = 238891845876279384611136653417072305750989037756361623415028512843158199445947367187435069338889013

BYTE_SIZE = 8                   # bits per byte
KEY = 295556873421021697574671957841159273934 #XOR-key for the chekpoint
# Return (x**d) % n.
def modular_exponentiation(x, d, n):
    if d == 0:
        return 1
    elif d % 2 == 0:
        y = modular_exponentiation(x, d // 2, n)
        return (y * y) % n
    else:
        return (modular_exponentiation(x, d-1, n) * x) % n

# Takes a bytes or bytearray object and converts it to an int.
# Character 0 of the bytes/bytearray should be in byte 0 (the rightmost
# byte) of the int when we are done.
def bytes_to_int(bytes):
    result = 0
    shift = 0

    for byte in bytes:
        result += byte << shift
        shift += BYTE_SIZE

    return result

# Takes an int x and converts it to a bytearray.  Byte 0 (the least significant
# byte of the int) becomes byte 0 of the bytearray.  Also takes as a parameter
# the number of bytes to include in the bytearray.
def int_to_bytes(x, size):
    result = bytearray()
    mask = 0xFF     # mask for isolating least significant byte

    for i in range(size):
        result.append(x & mask)
        x >>= BYTE_SIZE

    return result

# Generate a random pad for a given number of bytes.  Return the pad,
# represented as a bytearray.
def generate_pad(block_size):
    pad = bytearray()                       #make a bytearray
    for i in range(block_size):            #as long as the length of the bytearray doesn't exceed the size of the text block...
                                            #keep appending random integers to the pad
        pad.append(randint(0,255))

    return pad                              #return the pad




# XOR a block of bytes, byte by byte, with a key, which is a bytearray.
# The key must be at least as long as the block.
# Return the XORed block of bytes as a bytearray.
def xor_block(key, block):
    assert len(key) >= len(block)       #make sure the key is at least as long as the block it is going to XOR
    result = bytearray()                #create a bytearray to hold the result and save a reference to it in a variable
    for i in range(len(block)):         #iterate through the block of text
        result.append(block[i] ^ key[i])        #XOR every bit of the block with the corresponding bit of the ket and then append the result to the bytearray
    return result                               #return the result/bytearray





# Encrypt a plaintext file into a ciphertext file, using the hybrid cryptosystem.
# Parameters are the name of the plaintext file, the name of the ciphertext file,
# the exponent and modulus used for RSA encryption of the one-time pad, the
# number of bytes in the one-time pad, and the one-time pad (if None, then generate
# the one-time pad).
def encrypt_file(plaintext_file_name, ciphertext_file_name, e, n, block_size, pad = None):
    out_file = open(ciphertext_file_name, "wb")                 #open both files to read/write in bytes
    in_file = open(plaintext_file_name, "rb")
    if pad == None:
        pad = generate_pad(block_size)                      #generate a pad the same size as the size of the text block given as a parameter
    pad = bytes_to_int(pad)                             #turn this into an integer to use in modular exponentiation to encrypt it
    one_time_pad = modular_exponentiation(pad, e, n)
    new_pad = str(one_time_pad) + "\n"                        #concatonate a string of the pad with a newline character
    encrypted_pad = new_pad.encode()                        #turn it into bytes


    out_file.write (encrypted_pad)                       #write this encrypted pad as the first line of the textfile given as a paramet

    block = in_file.read(block_size)                    #read the first block of text
    pad = int_to_bytes(pad, block_size)                 #turn the ORIGINAL (not encrypted) pad back to bytes, as we need to use it to encrypt the text
    while len(block)>0:
        encrypted_text = xor_block(pad,block)              #xor each block of the text with the original pad we generated BEFORE encryption
        out_file.write(encrypted_text)                     #write the text into the second file
        block = in_file.read(block_size)                    #move on to the next chunk of text
    in_file.close()                                         #close both files
    out_file.close()


# Decrypt just a one-time pad from a file.  Assumes that the file is already open and
# that the caller will close the file.  The encrypted one-time pad is text that is
# the first line in the file.  Parameters are the file object, the exponent and modulus
# used for RSA decryption of the one-time pad, and the number of bytes in the one-time
# pad.  Returns the one-time pad as a bytearray.
def decrypt_pad(pad_file, d, n, block_size):
    integer = int(pad_file.readline())                          #read the first line of the pad_file given as a parameter
    one_time_pad = modular_exponentiation(integer, d, n)        #use modular exponentation on this integer, which returns another integer
    bytearray = int_to_bytes(one_time_pad, block_size)          #turn this integer into bytes- it is now a bytearray. Return it.
    return bytearray


# Decrypt a ciphertext file into a decrypted plaintext file, using the hybrid cryptosystem.
# Parameters are the name of the ciphertext file, the name of the decrypted plaintext file,
# the exponent and modulus used for RSA decryption of the one-time pad, the
# number of bytes in the one-time pad, and the one-time pad (if None, then read and
# decrypt the one-time pad from the ciphertext file).
def decrypt_file(ciphertext_file_name, decrypted_file_name, d, n, block_size, pad = None):
    in_file = open(ciphertext_file_name, "rb")                   #open the textfile given as a parameter to read in BYTES
    if pad == None:                                                 #if the pad is not given in the parameter, decrypt the first line of the textfile to get the pad
        pad = decrypt_pad(in_file, d, n ,block_size)


    block = in_file.read(block_size)                                #read a block of text from the textfile and save the reference to a variable
    out_file = open(decrypted_file_name, "wb")                      #open the second textfile given as a parameter, this time to write in
    while len(block) > 0:
        decrypted_text = xor_block(pad, block)                      #XOR this block of text with the pad and write it into the second textfile
        out_file.write(decrypted_text)
        block = in_file.read(block_size)                            #move on to the next block of text
    in_file.close()                                                 #close both files
    out_file.close()



#CHECKPOINT TEST HARNESS
# key= int_to_bytes(KEY, 16)                      #turn the given key into a bytearray of length 16 bytes
# b1 = bytearray("extraterrestial", "UTF-8")      #make a bytearray of a random string, make sure it is in ASCII code and save it to a variable
# xored_block = xor_block(key,b1 )                #XOR this bytearray of the string with the bytearray of the key. Save this to a variable
# print (xored_block)
# back_to_normal = xor_block(key, xored_block)        #repeat, but now the text being XORED is the already XORED text from before
# print (back_to_normal)                              #the text should be decrypted and should be the same as the original

decrypt_file("ciphertext1.txt", "decrypted_test_file",d, n, 128)




