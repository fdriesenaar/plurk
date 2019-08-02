from plurk.plurk import permu
from plurk.plurk import crypt
from plurk.plurk import decrypt
from plurk.plurk import xor

message="""Welkom World!"""

seed=12675681279995675689098798778
print(seed)
p=permu(message,seed=seed)
print(p)
x=xor(seed)
print(x)

encrypted=crypt(bytes(message,'utf-8'),p,xor=x)
print(encrypted)

decrypted=decrypt(encrypted,p,xor=x)
print(decrypted)    
