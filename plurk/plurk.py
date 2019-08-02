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

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def xor(seed):
    (d,m)=divmod(seed,256)
    return int_to_bytes(m)[0]

def crypt(message,permu,xor=None):
    crypted=bytes("",'utf8')
    for i in permu:
        i=i-1
        if xor is None:
            crypted=crypted+message[i]
        else:
            original_byte=message[i]
            xored_byte=original_byte ^ xor
            crypted=crypted+int_to_bytes(xored_byte)
        message=message[:i]+message[i+1:]
    return crypted

def decrypt(crypted,permu,xor=None):
    decrypted=bytes("",'utf8')
    permu.reverse()
    for i in permu:
        i=i-1
        if xor is None:
            decrypted=insert(decrypted,i,crypted[-1])
        else:
            original_byte=crypted[-1]
            xored_byte=original_byte ^ xor
            decrypted=insert(decrypted,i,int_to_bytes(xored_byte))
        crypted=crypted[:-1]
    return decrypted

def insert(into,pos,string):
    s=into[:pos]+string+into[pos:]
    return s

