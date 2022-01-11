import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
for led in range(60): #pick out indeces: led = 0,1,2,3...
    leds[led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)

led = 0
while led<60:
    leds[59-led] = (0,255,0)
    time.sleep(.1)
    client.put_pixels(leds)
    led = led + 1 #or reverse if you want

#led = 59
#while led>=0:
#    leds[led] = (0,255,0)
#    time.sleep(.1)
#    client.put_pixels(leds)
#    led = led - 1 #or reverse if you want

led = 0
while led<60: #scroll all rows at the same time
    for rows in range(3): #first three rows left to right
        leds[led + rows*60] = (0,0,255)
    for rows in range(3,6): #last three rows reversed (right to left)
        leds[59-led + rows*60] = (50,50,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

# reverse the last example.
# do a scroll from the middle to the outside - two pixels moving away from each other.
# reverse the scroll from the middle
# do a snake, 5 pixels long, returns to start when it hits the end
