def generate_key(n):
	letters = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'
	key = {}
	count = 0
	# for each character in letters
	for char in letters:
		# assign char keys to key dict, assign the remainder of the count + the num n, 
		# divided by the length of the letters (25)
		# this staggers all the letters by n without allowing the number to ever go above 25
		key[char] = letters[(count + n) % len(letters)]
		count += 1
	return key


def encrypt(key, message):
	cipher = ''
	for char in message:
		if char in key:
			cipher += key[char]
		else:
			cipher += char
	return cipher


def get_decryption_key(key):
	dkey = {}
	for char in key:
		dkey[key[char]] = char
	return dkey
	

key = generate_key(3)
dkey = get_decryption_key(key)


message = 'YOU ARE AWESOME'
cipher = encrypt(key, message)
print(cipher)
decrypted_cipher = encrypt(dkey, cipher)
print(decrypted_cipher)
