# decrypt.py
# Main code to decrypt text and video ciphertext files.

from crypto import decrypt_file, decrypt_pad

BLOCK_SIZE = 16             # characters per block

d = 143335107525767630766681992050243383450593422653797373240583295055192203309151620171296230900825953
n = 238891845876279384611136653417072305750989037756361623415028512843158199445947367187435069338889013   # replace by n from your secret key

decrypt_file("ciphertext1.txt", "decrypted1.txt", d, n, BLOCK_SIZE)
print("Decrypted ciphertext1.txt")
decrypt_file("ciphertext2.txt", "decrypted2.txt", d, n, BLOCK_SIZE)
print("Decrypted ciphertext2.txt")

pad_file = open("pad.txt", "rb")
pad = decrypt_pad(pad_file, d, n, BLOCK_SIZE)
pad_file.close()
decrypt_file("encrypted-video", "decrypted-video.mp4", None, None, BLOCK_SIZE, pad)
print("Decrypted encrypted-video")


