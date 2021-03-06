#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vigenere, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll

alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
key = u"schlüssel"

cipher = Vigenere()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)


def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

cm = cm0
cm.set_alphabet(al.ENGLISH)
cm.set_key("keys")
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep="-")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(u"かぎ")
plaintext = u"text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !"
encdec(cm, plaintext)

cm = UpperCase(cm)
alphabet = al.GREEK
cm.set_alphabet(alphabet)
cm.set_key(u"κλειδί")
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

'''
schweißgequältvomödentextzürnttypografjakob
geodcärkpewdwrjcqivguaclhßjfpäawdcküshqlict
schweißgequältvomödentextzürnttypografjakob
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
shmfdpmnormfkpnzkfclmlyjkgrwbwgospjjoqmnoejdyjrzoqejoer
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
dlgkd-ivlsw-bafmb-wnfwt-vsacc-sddor-elr
thistextisdividedbyblocksoflength
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
S pmno rmf-kpnzkfcl mlyjkgrwbw. Rzowc sbi : ^,&@$~(*;?&#. Rzkx'q ad!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Sn zwmskwb Ng togymbi uw dwc WWLIABM_QHDEPW_SN!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text きうばぶぼぽど ぬをべんお ょしろにゃだ づぼはぁよ げゐほさぐゃや そぶざけの かちぎゅらろじ ゑぷりとず !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΣΠΌΝΜ ΊΒΌΨΠ ΞΊΤ ΈΤΥΌΠ Ρ ΌΌΝΨΣΟΓΞΙ. (ΔΧΞΓΙΙΦ ΥΛΧΖΨΦ)
ΉΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΥΘΕΡΊΑ. (ΑΝΔΡΈΑΣ ΚΆΛΒΟΣ)
'''
