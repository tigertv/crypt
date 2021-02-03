========
SecretPy
========

|PyPIpkg| |PythonV| |PythonImplement| |Docs| |Downloads| |License| |Travis|

**Download:**

https://pypi.org/project/secretpy

**Documentation:**

https://secretpy.readthedocs.io

**Source code & Development:**

https://github.com/tigertv/secretpy

Description
===========

SecretPy is a cryptographic Python package. It uses the following classical cipher algorithms:

- ADFGX, ADFGVX
- Affine
- Atbash
- Autokey
- Bazeries
- Beaufort
- Bifid
- Caesar, Caesar Progressive
- Chaocipher
- Columnar Transposition, Myszkowski Transposition
- Keyword
- Nihilist
- Simple Substitution
- Playfair, Two Square(Double Playfair), Three Square, Four Square
- Polybius
- Rot13, Rot5, Rot18, Rot47
- Trifid
- Vic
- Vigenere, Gronsfeld, Porta
- Zigzag(Railfence)

Installation
============

To install this library, you can use pip:

.. code-block:: bash

	pip install secretpy

Alternatively, you can install the package using the repo's cloning and the make:

.. code-block:: bash

	git clone https://github.com/tigertv/secretpy
	cd secretpy
	make install

Usage
=====

Direct way
----------

The cipher classes can encrypt only characters which exist in the alphabet, and they don't have a state.

.. code-block:: python
	
	from secretpy import Caesar, alphabets

	alphabet = alphabets.GERMAN
	plaintext = u"thequickbrownfoxjumpsoverthelazydog"
	key = 3
	cipher = Caesar()

	print(plaintext)
	enc = cipher.encrypt(plaintext, key, alphabet)
	print(enc)
	dec = cipher.decrypt(enc, key, alphabet)
	print(dec)

	print('=====================================')

	print(plaintext)
	# use default english alphabet
	enc = cipher.encrypt(plaintext, key)
	print(enc)
	dec = cipher.decrypt(enc, key)
	print(dec)

	'''
	Output:

	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqirämxpsvryhuwkhodüögrj
	thequickbrownfoxjumpsoverthelazydog
	=====================================
	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
	thequickbrownfoxjumpsoverthelazydog
	'''

CryptMachine
------------

``CryptMachine`` saves a state. There are alphabet, key and cipher, they can be changed in anytime.
In the previous example, plaintext contains only characters existing in the alphabet i.e. without spaces.
To change the behaviour, you can use ``CryptMachine`` and decorators(``SaveAll``, ``RemoveNonAlphabet``), so it's a preferred way to do encryption/decryption:

.. code-block:: python
	
	from secretpy import Atbash, Caesar, CryptMachine, alphabets
	from secretpy.cmdecorators import SaveAll, RemoveNonAlphabet


	def encdec(machine, plaintext):
		print(plaintext)
		enc = machine.encrypt(plaintext)
		print(enc)
		dec = machine.decrypt(enc)
		print(dec)
		print("-----------------------------------")


	plaintext = u"thequickbrownfoxjumpsoverthelazydog"
	key = 3
	cipher = Caesar()

	cm = CryptMachine(cipher, key)
	encdec(cm, plaintext)

	cm.set_alphabet(alphabets.GERMAN)
	encdec(cm, plaintext)

	cm1 = SaveAll(cm)
	cm1.set_key(9)
	plaintext = u"the quick brown fox jumps over the lazy dog"
	encdec(cm1, plaintext)

	cm2 = RemoveNonAlphabet(cm)
	cm2.set_cipher(Atbash())
	plaintext = u"Achtung Minen"
	encdec(cm2, plaintext)


	'''
	Output:

	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
	thequickbrownfoxjumpsoverthelazydog
	-----------------------------------
	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqirämxpsvryhuwkhodüögrj
	thequickbrownfoxjumpsoverthelazydog
	-----------------------------------
	the quick brown fox jumps over the lazy dog
	üqn zßrlt käxbw oxc sßvyö xanä üqn ujed mxp
	the quick brown fox jumps over the lazy dog
	-----------------------------------
	Achtung Minen
	ßöwkjqxrvqzq
	achtungminen
	-----------------------------------
	'''

CompositeMachine
----------------

Combining several ciphers to get more complex cipher, you can use ``CompositeMachine``:

.. code-block:: python

	from secretpy import Rot13, Caesar, CryptMachine, CompositeMachine
	from secretpy.cmdecorators import SaveAll, RemoveNonAlphabet


	def encdec(machine, plaintext):
		print("=======================================")
		print(plaintext)
		enc = machine.encrypt(plaintext)
		print(enc)
		dec = machine.decrypt(enc)
		print(dec)


	key = 5
	plaintext = u"Dog jumps four times and cat six times"
	print(plaintext)

	cm1 = SaveAll(CryptMachine(Caesar(), key))
	enc = cm1.encrypt(plaintext)
	print(enc)

	cm2 = SaveAll(CryptMachine(Rot13()))
	enc = cm2.encrypt(enc)
	print(enc)

	print("=======================================")

	cm = CompositeMachine(cm1)
	cm.add_machines(cm2)
	enc = cm.encrypt(plaintext)
	print(enc)
	encdec(cm, plaintext)

	cm.add_machines(cm1, cm2)
	encdec(cm, plaintext)

	'''
	Output:

	Dog jumps four times and cat six times
	Itl ozrux ktzw ynrjx fsi hfy xnc ynrjx
	Vgy bmehk xgmj laewk sfv usl kap laewk
	=======================================
	Vgy bmehk xgmj laewk sfv usl kap laewk
	=======================================
	Dog jumps four times and cat six times
	Vgy bmehk xgmj laewk sfv usl kap laewk
	Dog jumps four times and cat six times
	=======================================
	Dog jumps four times and cat six times
	Nyq tewzc pyeb dswoc kxn mkd csh dswoc
	Dog jumps four times and cat six times

	'''

Maintainers
===========

- `@tigertv <https://github.com/tigertv>`_ (Max Vetrov)

.. Images and Links 

.. |PyPIpkg| image:: https://img.shields.io/pypi/v/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |PythonV| image:: https://img.shields.io/pypi/pyversions/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |PythonImplement| image:: https://img.shields.io/pypi/implementation/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |Docs| image:: https://img.shields.io/readthedocs/secretpy.svg?style=flat-square
	:alt: Read the Docs
	:target: https://secretpy.readthedocs.io/en/latest
.. |Downloads| image:: https://img.shields.io/pypi/dm/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |License| image:: https://img.shields.io/github/license/tigertv/secretpy.svg?style=flat-square
	:alt: Go to Github
	:target: https://github.com/tigertv/secretpy
.. |Travis| image:: https://img.shields.io/travis/tigertv/secretpy/master.svg?style=flat-square
	:alt: Go to Travis
	:target: https://travis-ci.org/tigertv/secretpy

