import opc
from time import sleep
import colorsys

leds = [(0,0,0)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness
start_hue = 50 #colour vals

for i in range(60): #this decides the final value(kind of)
	rgb_fractional = colorsys.hsv_to_rgb(((start_hue+i)*2)/360.0, s, i/60) #colorsys returns floats between 0 and 1
	r,g,b = rgb_fractional #extract said floating point numbers and convert to rgb range
	leds[i] = (r*255,g*255,b*255)
client.put_pixels(leds) #assign
sleep(0.2)