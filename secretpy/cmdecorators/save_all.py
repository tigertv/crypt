#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveAll(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__crypt(text, self._machine.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self._machine.decrypt)

    def __crypt(self, text, func):
        # make lower case and save indexes
        upcases = [i for i, c in enumerate(text) if c.isupper()]
        txt = text.lower()

        # prepare alphabet
        alphabet = self._machine.get_alphabet()
        alpha = {c: 1 for letters in alphabet for c in letters}

        # save indexes of non-alphabet characters
        chars = [i for i, c in enumerate(txt) if c not in alpha]

        # execute function
        res = list(func(txt))

        # restore non-alphabet characters
        for i in chars:
            res.insert(i, text[i])

        # restore uppercase
        for i in upcases:
            res[i] = res[i].upper()

        return "".join(res)
