import serial
import time

arduino=serial.Serial('COM5', 9600) #check com on windows; for mac, check what /dev/tty port it uses.

time.sleep(2)


while True:
	data = int(arduino.readline().decode('utf-8')) # works for default println behaviour. use str() if you're sending large datasets.
	print(data)