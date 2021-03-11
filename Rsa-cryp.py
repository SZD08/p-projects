# Understanding RSA #

# RSA modulus is => n=p*q
# Totient => (p-1)*(q-1)
# d = e^-1 mod ((p-1)(q-1))
# Encryption Formula => C = Plaintext^e mod n
# Decryption formula => M = C^d mod n


from Crypto.Util.number import *

# uncomment when needed 

q = ''
p = ''
n = ''
e = ''
d= ''
ciphertext = ''
plaintext = ''

#
#
# PROBLEM #1 : To find n from p & q
#print(p*q)
#
#
# PROBLEM #2 : To find q from p & n 
#print(n/p)
#
#
# PROBLEM #3 : To find totient with p & q 
#print((p-1)*(q-1))
#
#
# PROBLEM #4 : To find ciphertext(c) with plaintext, e & n 
#c = plaintext**e % n 
#print(c)
#
#
# PROBLEM #5 : To find d with e, p & q 
#print(inverse(e,((p-1)*(q-1))))
#
#
# PROBLEM #6 : To find plaintext with ciphertext, p, e & n 
#q = n/p
#d = inverse(e,((p-1)*(q-1)))
#plain = pow(ciphertext,d,n)
#print(plain)
