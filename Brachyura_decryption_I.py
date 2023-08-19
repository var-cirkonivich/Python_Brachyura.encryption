# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:13:17 2023

@author: Pakhomav
"""

def decrypt_text(text, key, num):
    decrypted_text = []
    decrypted_k = 0
    for char in text:
        decrypted_char = chr((ord(char) - int(key[num]) - decrypted_k) % 1114112)
        decrypted_text.append(decrypted_char)
        decrypted_k += 1
    return ''.join(decrypted_text)

def decrypt_text2(text, key, num):
    decrypted_text = []
    decrypted_k = 0
    for char in text:
        decrypted_char = chr((ord(char) + int(key[num]) - decrypted_k) % 1114112)
        decrypted_text.append(decrypted_char)
        decrypted_k += 1
    return ''.join(decrypted_text)

def decrypt_text3(text, key):
    decrypted_text = []
    decrypted_k = len(text)
    for char in text:
        decrypted_char = chr((ord(char) + decrypted_k) % 1114112)
        decrypted_text.append(decrypted_char)
        decrypted_k -= 1
    return ''.join(decrypted_text)

def keytu(key):
    keyds = []
    keyt = str(key)
    keyds += keyt
    keyt = str(key % 77)
    keyds += keyt
    keyt = str(key // 23)
    keyds += keyt
    keyt = str(key*5 % 77)
    keyds += keyt
    keyt = str(key*7 // 23)
    keyds += keyt
    keyt = str(key // 777)
    keyds += keyt
    keyt = str(key * 29)
    keyds += keyt
    return keyds

if __name__ == "__main__":
    filename = input("Please enter the file name to decrypt: ")
    keyw = int(input("Please enter the key (integer): "))
    key = keytu(keyw)
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    decrypted_content = decrypt_text(content, key, 6)
    decrypted_content = decrypt_text2(decrypted_content, key, 5)
    decrypted_content = decrypt_text(decrypted_content, key, 4)
    decrypted_content = decrypt_text2(decrypted_content, key, 3)
    decrypted_content = decrypt_text2(decrypted_content, key, 2)
    decrypted_content = decrypt_text2(decrypted_content, key, 1)
    decrypted_content = decrypt_text3(decrypted_content, key)
    decrypted_content = decrypt_text(decrypted_content, key, 0)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(decrypted_content)

