from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys
from hashlib import sha256

# The high level verify algorithm is to take your public key, message, 
# and signature and ensure that the output of sign_pk(msg) = signature

def sign(m):
    #generate public key
    gen_keypair(curve=ecdsa.SECP256k1)
    private_key = gen_private_key(curve)
    #public_key = get_public_key(private_key, curve)
    public_key=1
    print("public key:")
    print(public_key)
    #generate signature
    r = 0
    s = 0
    return( public_key, [r,s] )


# The python interpreter actually executes the function body here
# print("Answer: ")
# sign(m)