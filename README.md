# plurk
Plurk - encrypting as strong as you want

# Encryption

I am exploring some encryption ideas. The first one I want to elaborate on here is to encrypt a message by permuting its content based on a 'secret': something that determines the permutation, let's call it a permu.

For example, say you have a message "Hoi" and permu (3,1), this would be encoded as "iHo";
first the 'i' because it is the 3-rd letter and then the 'H', being the 1-st one leaving 'o' as the last one.

# Permu

From the example we can see that given a message of lenght n, a permu consists of n-1 numbers, where each number is at the most 1 smaller than it's predecessor, the first one being n at the most.

# Generating the permu

I included a python function which generates a permu based on a (big) number and subsequently uses this to encrypt and decrypt a message with the option to xor the encrypted result.
It generates the following output:

	12675681279995675689098798778
	[10, 11, 5, 10, 8, 8, 3, 3, 4, 3, 3, 2, 1]
	186
	b'\xc8\xde\xd5\x9b\xd5\xd6\xd6\xd1\x9a\xd7\xed\xdf\xed'
	b'Welkom World!'
