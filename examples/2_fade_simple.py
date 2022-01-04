import opc
from time import sleep

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360           # list of 360 tuples, each containing R,G,B values.
fade_amount = 5                     # size of each fade step.
print(led_list)
print(enumerate(led_list))
while True:
    for led in enumerate(led_list): # enumerate creates a list of tuples that contain index and contents of each element
                                    # in our case: led = (led_num, (R,G,B))
        r,g,b = led[1]              # this points to the second element in led - the (R,G,B) tuple.
        r = r+fade_amount
        g = g+fade_amount
        b = b+fade_amount

        new_colour = (r,g,b)            # create new tuple containing the updated values
        led_list[led[0]] = new_colour   # place it in the original list at index led_num.

        if r >=255 or r <= 0:           # check if the fade has hit its' limit;
            fade_amount = -fade_amount  # if it has - change directions from the next iteration.

    client.put_pixels(led_list)         # send the entire new list to the lights.
    sleep(.02)                          # 20ms delay