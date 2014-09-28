from Crypto.Cipher import AES
#from argparse import ArgumentParser
import string

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():
	primeNumber = 340282366920938463463374607431768211297
	generator = 339661812359158752487805590648382723243
	resultAlice = 197539712888466083939816614150725609070
	x = 1
	while (((generator * x ) % primeNumber) != resultAlice):
		x=x+1
		print x
	print x
	# print "iterater %d" % x
	# if(((generator * x ) % primeNumber) == resultAlice):
	# 	print x
		
	# x=x+1
   	# print "the while was breaken"
	# n0 = primeNumber
	# t0 = 0
	# t = 1
	# b = resultAlice/float(generator)
	# q = n0/float(b)
	# print q
	# print n0
	# r = float((n0 - q))*float(b)
	# print r
	# while r > 0:
 # 		temp = (t0 - q)*t
	# 	if temp >=0: 
	# 		temp = temp % primeNumber
	#    	else: 
	#    		temp = primeNumber - ((-temp) % primeNumber)
	# 	t0 = t
	# 	t = temp
	# 	n0 = b
	# 	b = r
	# 	q = n0/float(b)
	# 	r = (n0 - q)*b
	# if b != 1:
	# 	print ("b nao possui inverso multiplicativo")
	# 	print b
	# else:
	# 	print t


main()