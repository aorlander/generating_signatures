from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

def sign(m):
    #generate public key
    public_key=0
    print("Hello")
    #generate signature
    r = 0
    s = 0
    return( public_key, [r,s] )


# The python interpreter actually executes the function body here
# print("Answer: ")
sign(m)