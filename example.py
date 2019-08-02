from plurk.plurk import permu
from plurk.plurk import crypt
from plurk.plurk import decrypt

message="Hello World!"
seed=126756812799956756
print(seed)
p=permu(message,seed=seed)
print(p)

encrypted=crypt(message,p)
print(encrypted)

decrypted=decrypt(encrypted,p)
print(decrypted)    
