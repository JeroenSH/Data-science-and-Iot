import sys
import os
import serial
import time

#settings for setting up serial port
ser          = serial.Serial()
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS
ser.parity   = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff  = 1
ser.rtscts   = 0
ser.timeout  = 30
ser.port     = '/dev/ttyUSB0'

try:
    ser.open()                                          # try opening serial port
except:
    print("unable to open serial port")

start = time.time()
i = 0
fb = open('log.txt','w')
fb.write(start)
fb.close()
while i < 180:
#     print(time.time() -start)
    if time.time() - start >= 10:
	start = time.time()
        # do something here
	fb = open('log.txt','a+')
	for j in range(20):
		fb.write(ser.readline()) 
		fb.write('\n')
	fb.write('\n')
	fb.close()
	i +=1
