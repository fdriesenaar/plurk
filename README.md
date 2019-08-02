# plurk
Plurk - encrypting as strong as you want

# Encryption

I am exploring some encryption ideas. The first one I want to elaborate on here is to encrypt a message by permuting its content based on a 'secret': something that determines the permutation, let's call it a permu.

For example, say you have a message "Hoi" and permu (3,1), this would be encoded as "iHo";
first the 'i' because it is the 3-rd letter and then the 'H', being the 1-st one leaving 'o' as the last one.

# Permu

From the example we can see that given a message of lenght n, a permu consists of n-1 numbers, where each number is at the most 1 smaller than it's predecessor, the first one being n at the most.

# Generating the permu

Of course, no one is going to generate (or communicate) the permu in this form, so the next thing to find a way to generate this permu from a pass phrase or other way.
