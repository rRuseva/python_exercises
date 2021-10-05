import os
import sys
import argparse
import math

### finding the prime positions in the given text
### returns a list with prime nubers(positions) form 0 to n, where n is the lenght of the given text
def primes_in_range(n):
	count = 0
	primes = []
	for num in range(1,n+1):  
		if num > 1:  
			for i in range(2,int(math.sqrt(num)) + 1):  
				if ((num % i) == 0):  
					break;
			else:  
				count += 1
				primes.append(num)
	return primes

### single fase decoding 

def decode_single_faze(text):
	text_len = len(text)
	primes = primes_in_range(text_len)
	primes_count = len(primes)
	# print("text len -{} \n primes - {} \n primes count - {}".format(text_len, primes, primes_count))
	result_text = [None]*text_len
	
	### setting the chars on prime positions	
	i = 0
	for i in range(primes_count):
		result_text[primes[i]- 1] = text[i]

	### seting other chars 
	result_text[0] = text[primes_count]
	j = primes_count + 1
	for i in range(text_len):
		if(result_text[i] == None):
			result_text[i] = text[j]
			j = j +1 

	# print(''.join(result_text))
	return ''.join(result_text)



def decode(k, text):
	result_text = []
	while k > 0:
		print("fase {}: {}".format(k, text))
		result_text = decode_single_faze(text)
		k = k - 1
		text = result_text
	return result_text


if __name__ == '__main__':

	### reads the arguments 
	ap = argparse.ArgumentParser(description="Decoding text with k phases of encoding")
	ap.add_argument("file_path", help="path to the encoded file")
	args = ap.parse_args()

	if args.file_path is not None:
		input_file_path = args.file_path
# else:
# 	input_file_path = input("Please enter the file path ")

### reading the text file 
with open(input_file_path, 'r') as file_obj:
	content = file_obj.readlines()
	if len(content) == 2:
		k = int(content[0])
		text = content[1]
		

decoded_text = decode(k, text)
print("decoded text: {}".format(decoded_text))
