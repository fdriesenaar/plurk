# plurk
Plurk - encrypting as strong as you want

# Encryption

I am exploring some encryption ideas. The first one I want to elaborate on here is to encrypt a message by permuting its content based on a 'secret': a (big) number that determines the permutation, let's call it a permu.

For example, say you have a message "Hoi" and permu 31, this would be encoded as "iHo";
first the 'i' because it is the 3-rd letter and then the 'H', being the 1-st one leaving 'o' as the last one.

So, before I will start working on a Python implementation of this method I first need some time offline to get my head around the 'permu'; it works for this simple example, but how about larger texts? How do you determine the permu for larger texts and how can you make it more human friendly (eg character based)?

To be continued.
