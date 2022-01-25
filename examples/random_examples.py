import opc
from time import sleep
import colorsys
import random

leds = [(0,0,0)]*360 #black

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness


# for led in range(360):
# 	leds[led] = (random.randint(0, 256),127,random.randint(0, 256))
# 	client.put_pixels(leds) #send out
# 	sleep(0.1)

# sleep(5000)

for hue in range(360):
    rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-10, hue+10)/360.0, s, v) #colorsys returns floats between 0 and 1
    r_float = rgb_fractional[0] #extract said floating point numbers
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]

    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
    leds[hue]=rgb
    client.put_pixels(leds) #send out

    sleep(0.03) #20ms 