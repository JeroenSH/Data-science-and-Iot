import sys
import os
import serial


#settings for setting up serial port
ser          = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity   = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff  = 1
ser.rtscts   = 0
ser.timeout  = 30
ser.port     = 'com13'

try:
    ser.open()                                          # try opening serial port
except:
    sys.exit ("error opening the serial port %s. "  % ser.name)

for i in range(10):
    try:
        data_raw = ser.readline()                       #read the serial port
    except:
        sys.exit("error reading serial port%s" % ser.name )
        ser.close()                                     #close the serial port

    data_line = ''.join(chr(ch & 0x7f) for ch in data_raw).strip()      #decoding stuff
    print(data_line)

ser.close()
print("program finished")