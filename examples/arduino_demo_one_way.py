import serial # if missing - in command prompt or terminal - pip install pyserial
import time

arduino= serial.Serial('COM5', 9600) #check com on windows; for mac, check what /dev/tty port it uses.
time.sleep(2)

#example for multiple input
#pot1, pot2, ldr = int(data.split(',')) #  "255, 407, 0" = ["255", "407", "0"] = [255, 407, 0]

while True:
	data = arduino.readline().decode('utf-8') # works for default println behaviour. use str() if you're sending large datasets.
	print(data)