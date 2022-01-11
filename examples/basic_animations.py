import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

leds[10] = (255, 0, 0)

time.sleep(3)
client.put_pixels(leds)
client.put_pixels(leds)

leds[10+60] = (255, 0, 0)

time.sleep(3)
client.put_pixels(leds)
client.put_pixels(leds)
