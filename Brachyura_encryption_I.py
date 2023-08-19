# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:44:55 2023

@author: Pakhomav
"""

def encrypt_text(text, key, num):
    encrypted_text = []
    encrypted_k = 0
    for char in text:
        encrypted_char = chr((ord(char) + int(key[num]) + encrypted_k) % 1114112)
        encrypted_text.append(encrypted_char)
        encrypted_k += 1
    return ''.join(encrypted_text)

def encrypt_text2(text, key, num):
    encrypted_text = []
    encrypted_k = 0
    for char in text:
        encrypted_char = chr((ord(char) - int(key[num]) + encrypted_k) % 1114112)
        encrypted_text.append(encrypted_char)
        encrypted_k += 1
    return ''.join(encrypted_text)

def encrypt_text3(text, key):
    encrypted_text = []
    encrypted_k = len(text)
    for char in text:
        encrypted_char = chr((ord(char) - encrypted_k) % 1114112)
        encrypted_text.append(encrypted_char)
        encrypted_k -= 1
    return ''.join(encrypted_text)

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
    key = []
    filename = input("Please enter the file name to encrypt: ")
    keyw = int(input("Please enter the key (integer): "))
    key = keytu(keyw)
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    encrypted_content = encrypt_text(content, key, 0)
    encrypted_content = encrypt_text3(encrypted_content, key)
    encrypted_content = encrypt_text2(encrypted_content, key, 1)
    encrypted_content = encrypt_text2(encrypted_content, key, 2)
    encrypted_content = encrypt_text2(encrypted_content, key, 3)
    encrypted_content = encrypt_text(encrypted_content, key, 4)
    encrypted_content = encrypt_text2(encrypted_content, key, 5)
    encrypted_content = encrypt_text(encrypted_content, key, 6)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(encrypted_content)


