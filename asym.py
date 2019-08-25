def decrypt(y,private_key):
    aa=private_key['aa']
    ba=private_key['ba']
    f=private_key['f']

    x=(f*y-ba)/aa
    return x

def encrypt(x,public_key):
    a=public_key['a']
    b=public_key['b']
    c=public_key['c']
    d=public_key['d']
    e=public_key['e']

    x2=x*x
    y=(a*x2+b*x+c)/(d*x+e)
    return y

def generate_pair(aa=1,ba=1,da=1,ea=1,f=1):
    pair={}
    private={
        'aa': aa,
        'ba': ba,
        'da': da,
        'ea': ea,
        'f': f
        }

    d=f*da
    e=f*ea
    a=aa*d
    b=aa*e+ba*d
    c=ba*e
    public={
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e
    }

    pair['private']=private
    pair['public']=public
    return pair

pair=generate_pair()
print(pair)
x=1
y=encrypt(x,pair['public'])
print(x,y)
z=decrypt(y,pair['private'])
print(x,y,z)

