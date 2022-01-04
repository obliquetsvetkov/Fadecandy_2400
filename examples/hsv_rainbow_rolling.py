import opc
from time import sleep
import colorsys
import numpy

client = opc.Client('localhost:7890')
#client = opc.Client('192.168.2.1:7890')

s = 1.0 #saturation max 1.0 so i don't have to redefine calculations as floating point later on 
v = 1.0 #value max 
pixels = [] #start empty

for hue in range(360): # shift through the entire colour spectrum
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #colorsys returns floats between 0 and 1
    print(rgb_fractional) # this is a tuple of 3 elements, R, G, B, set to 0-1 (representing 0-255)

    r_float = rgb_fractional[0] #extract said floating point numbers
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]

    #r_float, g_float, b_float = rgb_fractional 
    # this only works if the number of variables is the same as the length of the list (or tuple)


    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
    #if hue == 0:
    #    pixels.append((255,255,255)) #insert white dot at position 0.
    #else:
    pixels.append(rgb) #for loop runs 360 times; each LED gets a slightly different hue. 
    #we have a rainbow of 360 LEDs in a list, ready to be shifted around

while True:
    for i in range(360):
        client.put_pixels(pixels)
        # This rolls the entire tuple forward.
        #print pixels #debug
        pixels = numpy.roll(pixels,3) #roll by 3 because func seems to not care about tuples and rolled elements from them by 1.
        sleep(0.02) #speed of animation controlled through this