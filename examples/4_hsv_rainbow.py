import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(0,0,0)]*360

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness

for hue in range(360):
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #colorsys returns floats between 0 and 1
    print(rgb_fractional)
    r_float = rgb_fractional[0] #extract said floating point numbers
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]

    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
    print(rgb)
    leds[hue] = rgb 
    client.put_pixels(leds) #send out

    sleep(0.03) #20ms 