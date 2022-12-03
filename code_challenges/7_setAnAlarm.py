# -*- coding: utf-8 -*-
"""
Code challange #7 - Set alarm: 

Write Python function to play a sound and print a message at a set time.

Input: alarm time, sound file, message;
"""
import os
import sched
import time
from playsound import playsound


def set_alarm(alarm_time, sound, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    
    s.enterabs(alarm_time, 1, playsound, argument=(sound,))
    
    print("Alarm set for ", time.asctime(time.localtime(alarm_time)))
    s.run() 

if __name__ == '__main__':
    sound_path = os.path.join(os.getcwd(),'data','Train_ft._Nora-Shake_Up_Christmas_RingtoneSMS.mp3')
    set_alarm(time.time()+1, sound_path, 'It is christmas timeee !')