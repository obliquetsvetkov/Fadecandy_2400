#!/usr/bin/env python
#BMI calculator and Indicator

from __future__ import division 

import opc
import colorsys
from time import sleep
from random import seed
from random import randint


 



led =[(255,255,255)]*360  #led list for storage of hues
main = [(0,0,0)]*360  #main list that will be used
calci = [(0,0,0)]*360  #list for bmi calculator
calci1 = [(0,0,0)]*360  #list for bmi indicator
binary = []

#to use simulator
client = opc.Client('localhost:7890')



#to use actual leds

#client = opc.Client('192.168.2.1:7890')


def put_pixels():
    
    client.put_pixels(led)
    
def lightitup():
    
    client.put_pixels(main)
    
def answer():
    
    client.put_pixels(calci)
def display():
    client.put_pixels(calci1)
for t in range(0,2):
    
    print("Please enter a number")
    num = int(input())

    fn = bin(num)[2:] #Converting into binary and removing 0b from it
    

    binary = [int(index) for index in fn] #list comprehension

    print (binary)

    ledb = 0
    
    for lb in binary:
        
            
            if lb ==0:
                main[ledb] = (255,0,0) #red is for zero
                ledb+=1
                
                
            else:
                main[ledb] = (0,0,255) #blue is for one
                ledb+=1
            
            
    lightitup()
    sleep(5)
    main = [(0,0,0)]*360
    lightitup()
    print("done")
    
        
    
