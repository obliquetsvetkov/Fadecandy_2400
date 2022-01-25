#OPC stuff:
import opc
import time
import random

leds = [(255,255,255)]*360 #set first colours; optional. Make an empty list at least.

client = opc.Client('localhost:7890') #connect to sim
client.put_pixels(leds) #display the first colours (if set)
client.put_pixels(leds)

#-----------------------------------------------------------------------------------------------------------
#tkinter stuff:
import tkinter as tk #shorter name to use for all the methods

window = tk.Tk() #main window object - this will generate the window for our gui.
window.title('OPC TKInter Demo')


#-----------------------------------------------------------------------------------------------------------
#command definitions for below buttons:
def sweepfwd():
    for led in range(360): #pick out indeces: led = 0,1,2,3...
        leds[led] = (255,0,0)
        time.sleep(0.1)
        client.put_pixels(leds)

def sweeprows():
    led = 0
    while led<60: #scroll all rows at the same time
        for rows in range(3): #first three rows left to right
            leds[led + rows*60] = (0,0,255)
        for rows in range(3,6): #last three rows reversed (right to left)
            leds[59-led + rows*60] = (50,50,255)
        client.put_pixels(leds)
        time.sleep(0.1)
        led = led + 1
    
def snake():
    i = 0
    while i < 3:
        rand_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for led in range(0, 360):
            leds = [(255,255,255)]*360  #white  #set everything white,
            rand_color = (random.randint(rand_color[0]-50, rand_color[0]+50),random.randint(rand_color[1]-50, rand_color[1]+50),random.randint(rand_color[2]-20, rand_color[2]+20))
            leds[355-led] = rand_color       #set 5 leds another colour, incrementing position each frame
            leds[355-led+1] = rand_color
            leds[355-led+2] = rand_color
            leds[355-led+3] = rand_color
            leds[355-led+4] = rand_color
            if led == 355:              #if we reach the end go back;
                led = 0
            client.put_pixels(leds)     #place the latest frame on screen.
            time.sleep(0.1)            #delay the frame a bit
        i += 1

#-----------------------------------------------------------------------------------------------------------
#geometry:

window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, weight = 3)

#-----------------------------------------------------------------------------------------------------------
#widgets:
anim1_button = tk.Button(window, text = 'Sweep singles', command = sweepfwd)
anim2_button = tk.Button(window, text = 'Sweep all rows', command = sweeprows)
anim3_button = tk.Button(window, text = 'Snake', command = snake)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy) #destroy the window, closing the program.

#-----------------------------------------------------------------------------------------------------------
#layout:
anim1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
anim2_button.grid(column = 1, row = 1, padx = 5, pady = 5)
anim3_button.grid(column = 2, row = 1, padx = 5, pady = 5)
exit_button.grid(column = 2, row = 2, sticky='e', padx = 5, pady = 5)

window.mainloop()


