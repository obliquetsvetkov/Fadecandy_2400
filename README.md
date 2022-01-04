# Fadecandy_2400

## Simulator

The simulator provided has 360 leds arranged in a grid pattern of 6 rows with 60 leds each.

###### Basic commands
```
opc.Client() - sets up a client object that will establish communication between Python and a fadecandy server.
Required argument: an IP or localhost with correct port for the server.
```

```
.put_pixels(list) - places a list of tuples with rgb values to the fadecandy server to be displayed.
Format: [(R_value, G_value, B_value)]. Each tuple element in the list represents a single led.
```

There are a few more methods for ensuring connection and disconnect procedures, but they will not be needed with the simulator.

###### Notes

To connect to the simulator, use localhost with port 7890 when setting up your fadecandy instance in Python: 
```
client = opc.Client('localhost:7890')
```

When not using a loop, perform .put_pixels() twice to avoid interpolation issues:
```
client.put_pixels(list)
client.put_pixels(list)
```

It's highly recommended to perform any colour fading in an HSV space as opposed to RGB. Refer to the '4_hsv_rainbow.py' and 'hsv_rainbow_rolling.py' examples. Keep Value (saturation) max to begin with, play with the value for more pastel, washed out colours.  

## Other files

- 60by6.jpg - use this as a template to easily plan templates and check led numbers.
- colour spaces.pdf - basic information on the difference between RGB and HSV. 
- Fadecandy exercises.pdf - some simple tasks to get you started.
