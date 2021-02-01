import sys
import os
import serial
import time
import requests

def addDataToUrl(url,data, index):                                      #function to add the data to the url
    url += '&field' + str(index) + '=' + str(data)
    return url

types = ['1.8.1', '1.8.2','2.8.1','2.8.2','1.7.0','2.7.0']

#settings for setting up serial port
ser          = serial.Serial()
ser.baudrate = 9600 
ser.bytesize = serial.SEVENBITS
ser.parity   = serial.PARITY_EVEN
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff  = 1
ser.rtscts   = 0
ser.timeout  = 30
ser.port     = '/dev/ttyUSB0' 


print("program started")
try:
    ser.open()                                          # try opening serial port
except:
    print("unable to open serial port")

start = time.time()

while True:
    if time.time() - start >= 20:                                   #timer to read the serial port every 20 seconds and not all the time.   
	start = time.time()
	
        url = 'https://api.thingspeak.com/update?api_key=CYDAGE3RHPJUTR7F'
	while True:
		data_raw = ser.readline()		
		if '!'  in data_raw:			#end of sending data
			break	                        #break stops the current while loop and 
		
		start_type = data_raw.find(":") + len(":")	#split the line in type 
		end_type = data_raw.find("(")
		type = data_raw[start_type:end_type]
		
		start_data = data_raw.find("(") + len("(")      #split the line in data
		end_data = data_raw.find(")")
		data = data_raw[start_data :end_data] 
		if type in types:                               #check for the correct type in the data and append it to the URL
			index = 1+ types.index(type)
			url = addDataToUrl(url,data,index)
	res = requests.post(url)                                #post the URL so it will be send to Thingspeak
	
print("program finished")
