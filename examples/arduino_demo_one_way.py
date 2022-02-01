import serial
import time

arduino=serial.Serial('COM5', 9600) #check com on windows; for mac, check what /dev/tty port it uses.

time.sleep(2)


while True:
	data = int(arduino.readline().decode('utf-8')) # make sure to terminate the line with a '\n' symbol from arduino (should be default)
	print(data)