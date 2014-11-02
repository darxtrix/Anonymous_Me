#!/usr/bin/python

'''
Converts the decimal valued primary_id of the url database table to a unique string by base62 conversion

0 -> 0
1 -> 1
.
A -> 11
B -> 12
.
a -> 37
b -> 38

A bijective mapping is used for this purpose 
'''
TOKENS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

BASE = 62 # 26*2 + 10 = 62 , 26 small english alphabets , 26 capital english alphabets and 10 digits

DIGITS_OFFSET = 48
SMALL_OFFSET = 61
LARGE_OFFSET = 55

hashed_value = [] # this will contain the shortified url


def order(remainder):
	'''
		Does mapping of tokens to remainder for base62 conversion 
	'''
	if remainder <= 9:
		return chr(DIGITS_OFFSET+remainder)
	elif remainder <= 35:
		return chr(LARGE_OFFSET+remainder)
	else:
		return chr(SMALL_OFFSET+remainder)
	


def convert(number):
	''' 
	Recursive function to compute the base62 number of a given integer
	'''
	if number == 0:
		return
	rem = number%62
	number = number/62
	hashed_value.append(order(rem))
	convert(number)

def hashed_string(number):
	'''
		Returns the hash value as  a string
	'''
	convert(number)
	hash_value = ''.join(hashed_value)
	return hash_value

def hstring_to_id(hstring):
	'''
		Returns the id by taking a hash value
	'''
	id = 0
	for ctr in range(len(hstring)):
		id += TOKENS.index(hstring[ctr])*(62**ctr)
	return id

if __name__ == '__main__':
	n = raw_input("Enter an integer to be converted to base62 notation : ")  # fix leading 0 that makes the input qualify as an octal number
	n = int(n)
	print hashed_string(n)










