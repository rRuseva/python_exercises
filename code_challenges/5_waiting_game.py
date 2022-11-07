# -*- coding: utf-8 -*-
"""
Code challange #5 - Waiting game : 

Write Python program that gives the user random amount of seconds ( between 2 and 4)
Waits the user to press Emter and starts counting the time untill the key is pressed second time.


Outputs the time passed between the two presses.

"""
import time 
from random import randint
import math

def waiting_game():
	target_time = randint(2,4)
	print("Your target time is {}\n\n".format(target_time))
	input("--- Press Enter to begin ---")
	time_start = time.time()
	input("... Press Enter again after {} seconds ...".format(target_time))
	time_end = time.time()
	your_time = time_end - time_start
	off_time = abs( your_time - target_time)
	print("Elapsed time: {} seconds ( {} seconds off time)".format(your_time, off_time))

if __name__ == '__main__':
    waiting_game()
    
    
    