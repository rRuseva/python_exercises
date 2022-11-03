# -*- coding: utf-8 -*-
"""

Code challanges from LinkedIn Learning video : 8 Things You Must Know in Python

"""
import string

def contains_punctuation(phrase):
	""" Returns True if the given phrase contains punctuations.
	Otherwise returns False.
	"""
	return any(ch in string.punctuation for ch in phrase)

 
def anual_births_average(years,births):
	""" Return a list of tuples with each entry in the fowolling format: 
	(year, birth, running_average of births)
	Where runing_average is the avereg up to current year.
	Round the running_average to nearest integer. """
	
	result = []
	sum = 0
	for index, (year, birth) in enumerate(zip(years, births), start=1):
		sum += birth
		result.append((year, birth, round(sum/index)))
	return result

import re
def is_palindrome(phrase):
	""" returns True if the phrase is palindrome """
	text = phrase.lower()
	text = re.sub('\W+', '', text)
	return text == ''.join(reversed(text))



if __name__ == '__main__':
	### any() all challange
	# print(contains_punctuation('Readability counts') )
	# print(contains_punctuation('If the implementation is hard to explain, it\'s a bad idea.'))
	# print(contains_punctuation('There should be one-- and preferably only one --obvious way to do it.'))
	
	### enumerate() & zip() 
	# years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
	# births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

	# ## y,b, r_a = zip(*anual_births_average(years,births))
	# print(anual_births_average(years,births))
	# ## reulst should be: run_avg = [723165, 723539, 725584, 718816, 714099, 711392, 709231, 705466, 700089, 694117]
	# ## print(all(a==b for (a,b) in enumerate(zip(r_a,run_avg))))

	### test reverse: 
	print(is_palindrome('sagas'))
	print(is_palindrome('Radar'))
	print(is_palindrome('Was it a cat I saw?'))
	print(is_palindrome('Eva, can I see bees in a cave?'))
	print(is_palindrome('Red rum, sir, is MURDER!!'))
	print(is_palindrome("This should not not work") )
	print(is_palindrome('radars') )