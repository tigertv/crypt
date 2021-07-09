#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Autokey, alphabets


alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = "queenly"

cipher = Autokey()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"attackatdawn"

# use default english alphabet
print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
föiudtäßivamvhyyäeeüxüonhbwwzvßlwvk
thequickbrownfoxjumpsoverthelazydog
----------------------------------
attackatdawn
qnxepvytwtwp
attackatdawn
'''
