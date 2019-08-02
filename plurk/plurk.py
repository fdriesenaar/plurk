from math import sqrt
from math import trunc

def permu(message,seed=None):
    p=[]
    if seed is None:
        for n in range(len(message),0,-1):
            p.append(1)
    else:
        i=1
        for n in range(len(message),0,-1):
            brown=trunc(sqrt(seed*i))
            (d,m)=divmod(brown,n)
            m=m+1
            p.append(m)
            i=i+1
    return p

def crypt(message,permu):
    crypted=""
    for i in permu:
        i=i-1
        crypted=crypted+message[i]
        message=message[:i]+message[i+1:]
    return crypted

def decrypt(crypted,permu):
    decrypted=""
    permu.reverse()
    for i in permu:
        i=i-1
        decrypted=insert(decrypted,i,crypted[-1])
        crypted=crypted[:-1]
    return decrypted

def insert(into,pos,string):
    s=into[:pos]+string+into[pos:]
    return s

