#!/usr/bin/env python


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
    
    
answer()

"""creating a scale for bmi"""


for uw in range (0,19):
    for uw1 in range(0,3):
        calci[uw+60*uw1] = (255,255,52)#light yellow for underweight

for nw in range (19,25):
    for nw1 in range(0,3):
        calci[nw+60*nw1] = (50,205,50) #green for normalweight
    
for ow in range (25,30):
    for ow1 in range(0,3):
        calci[ow+60*ow1] = (255,165,0) #orange for risk of overweight
    
for ob in range (30,60):
    for ob1 in range(0,3):
        calci[ob+60*ob1] = (255,0,0) #red for overweight
    
for cc in range (0,180):
    calci1[cc] = calci [cc]


display()
    
#user interface start

for chance in range (0,2): #number of attempts if wrong.
    print("BMI CALCULATOR")
    print("Please enter your HEIGHT in centimeters:")
    h = int(input())
    h = h*0.01        #converting cm to m
    h = float(h*h)  


    print("Please enter your WEIGHT in kilograms:")

    w = int(input())
    w = float(w)
   
    bmi = w / h #formula

    bmi =round(bmi, 1) #value for display
    bmi1 =round(bmi) #value for list
    
    if h< 273 and w < 635:
        
            
            print ("Your BMI is:",bmi)
            print ("Blue blinking light indicates your BMI on the scale")
            sleep(1)
            if bmi1 <= 60:
                for q in range(0,20):
                    calci[bmi1] = (0,0,255)     #blue light
                    calci[bmi1+60] = (0,0,255)
                    calci[bmi1+60*2] = (0,0,255)
                    answer()
                    sleep(0.2)
                    display()
                    sleep(0.2)
                    
            elif bmi1 > 60:               #if the bmi exceeds 30   
                for con1 in range(0,20):
                    calci[59] = (0,0,255)
                    calci[119] = (0,0,255)
                    calci[179] = (0,0,255)
                    answer()
                    sleep(0.2)
                    display()
                    sleep(0.2)
                    
            break
    else:
        print("PLEASE ENTER CORRECT VALUES")
        










