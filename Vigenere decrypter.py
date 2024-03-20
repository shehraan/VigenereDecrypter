def decrypt_vigenere(ciphertext, keyword):
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    plaintext = ""
    for i in range(len(ciphertext)):
        shift = ord(keyword_repeated[i].upper()) - ord('A')
        ascii_offset = ord('A') if ciphertext[i].isupper() else ord('a')
        decrypted_char = chr((ord(ciphertext[i]) - ascii_offset - shift) % 26 + ascii_offset)
        plaintext += decrypted_char
    return plaintext

ciphertext = "SIMFITKXLLVOB"
keyword = "DEVDEGREE"
plaintext = decrypt_vigenere(ciphertext, keyword)
print(plaintext)
