from Crypto.Cipher import AES
#from argparse import ArgumentParser
import string

#def egcd(a, b):
#    if a == 0:
#        return (b, 0, 1)
#    else:
#        g, y, x = egcd(b % a, a)
#        return (g, x - (b // a) * y, y)
#
#def modinv(a, m):
#    g, x, y = egcd(a, m)
#    if g != 1:
#        raise Exception('modular inverse does not exist')
#    else:
#        return x % m

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def extEuclideanAlg(a, b) :
    """
    Computes a solution  to a x + b y = gcd(a,b), as well as gcd(a,b)
    """
    if b == 0 :
        return 1,0,a
    else :
        x, y, gcd = extEuclideanAlg(b, a % b)
        return y, x - y * (a // b),gcd

def modInvEuclid(a,m) :
    """
    Computes the modular multiplicative inverse of a modulo m,
    using the extended Euclidean algorithm
    """
    x,y,gcd = extEuclideanAlg(a,m)
    if gcd == 1 :
        return x % m
    else :
        return None

primeNumber = 340282366920938463463374607431768211297
generator = 339661812359158752487805590648382723243
resultAlice = 197539712888466083939816614150725609070
resultBob = 67715685814376960569898647713350694734
x = 1

print modInvEuclid(generator, primeNumber)
print resultAlice
