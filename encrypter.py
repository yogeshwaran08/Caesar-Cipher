import sys


def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result

if len(sys.argv) >= 2:    
	text = sys.argv[1]
	s = 6
	print("Text : " + text)
	print("Shift : " + str(s))
	print("Cipher: " + encrypt(text,s))