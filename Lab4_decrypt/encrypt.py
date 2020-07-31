# encrypt.py
# Main code to encrypt a plaintext file.

from crypto import encrypt_file
BLOCK_SIZE = 16

e = 11  # replace by e from the recipient's public key
n = 7591597157961497423304605451265683045390885464517418422351915771369120179455788035919092438122285007



encrypt_file("decrypted2.txt", "ciphertext_recitationleader.txt", e, n, BLOCK_SIZE, None)
print ("ciphertext.txt is made")


