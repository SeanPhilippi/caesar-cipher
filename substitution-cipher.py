from random import randint

def generate_key():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cletters = list(letters)
	key = {}
	for c in letters:
		key[c] = cletters.pop(randint(0, len(cletters) - 1))
	return key

def encrypt(key, message):
	cipher = ""
	for c in message:
		if c in key:
			cipher += key[c]
		else:
			cipher += c
	return cipher

def get_decrypt_key(key):
	dkey = {}
	# swap key and values in key to create dkey
	for k in key:
		dkey[key[k]] = k
	return dkey

key = generate_key()
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)

dkey = get_decrypt_key(key)
message = encrypt(dkey, cipher)
print('message', message)
