#opc stuff
import opc
import time
import random

leds = [(255,255,255)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

#tkinter stuff
import tkinter as tk
window = tk.Tk()
window.title('opc tkinter demo')

#functions:
def anim1():
    led = 0
    while led<60: #scroll all rows at the same time
        for rows in range(3): #first three rows left to right
            leds[led + rows*60] = (0,0,random.randint(127,255))
        for rows in range(3,6): #last three rows reversed (right to left)
            leds[59-led + rows*60] = (50,50,random.randint(127,255))
        client.put_pixels(leds)
        time.sleep(0.1)
        led = led + 1
        
def placeholder1():
    pass

def placeholder2():
    pass

window.rowconfigure(0, minsize = 20, weight = 1) #take up 3 spaces
window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, minsize = 20, weight = 1)

label = tk.Label(text = 'choose an animation:')
label.grid(row = 0, column = 0 )

anim1_button = tk.Button(window, text = 'anim 1', command =anim1)
anim2_button = tk.Button(window, text = 'anim 2', command =placeholder1)
anim3_button = tk.Button(window, text = 'anim 3', command =placeholder2)
exit_button = tk.Button(window, text = 'exit', command = window.destroy)

anim1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
anim2_button.grid(column = 1, row = 1, padx = 5, pady = 5)
anim3_button.grid(column = 2, row = 1, padx = 5, pady = 5)
exit_button.grid(column = 2, row = 2, padx = 5, pady = 5)

window.mainloop()
