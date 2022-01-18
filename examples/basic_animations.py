import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

# #for led in leds: # pick out an element: led = (255,255,255)
# for led in range(60): #pick out indeces: led = 0,1,2,3...
#     leds[led] = (255,0,0)
#     time.sleep(.1)
#     client.put_pixels(leds)

# led = 0
# while led<60:
#     leds[59-led] = (0,255,0)
#     time.sleep(.1)
#     client.put_pixels(leds)
#     led = led + 1 #or reverse if you want

# #led = 59
# #while led>=0:
# #    leds[led] = (0,255,0)
# #    time.sleep(.1)
# #    client.put_pixels(leds)
# #    led = led - 1 #or reverse if you want

# led = 0
# while led<60: #scroll all rows at the same time
#     for rows in range(3): #first three rows left to right
#         leds[led + rows*60] = (0,0,255)
#     for rows in range(3,6): #last three rows reversed (right to left)
#         leds[59-led + rows*60] = (50,50,255)
#     client.put_pixels(leds)
#     time.sleep(.1)
#     led = led + 1

# reverse the last example.
# do a scroll from the middle to the outside - two pixels moving away from each other.
# reverse the scroll from the middle
# do a snake, 5 pixels long, returns to start when it hits the end

while True:                         #do this forever:
    for led in range(355)           #for a range the size of our strip - 5: 
        leds = [(255,255,255)]*360  #white  #set everything white,
        leds[led] = (0,0,255)       #set 5 leds another colour, incrementing position each frame
        leds[led+1] = (0,0,255)
        leds[led+2] = (0,0,255)
        leds[led+3] = (0,0,255)
        leds[led+4] = (0,0,255)
        if led == 255:              #if we reach the end go back;
            led = 0
        client.put_pixels(leds)     #place the latest frame on screen.
        time.sleep(0.02)            #delay the frame a bit

what can we improve?