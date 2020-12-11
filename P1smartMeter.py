import sys
import os
import serial

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
    ser.open()
except:
    sys.exit ("Fout bij het openen van poort %s. "  % ser.name)

try:
    data_raw = ser.readline()
except:
    sys.exit("Fout bij lezen van poort %s" % ser.name )
    ser.close()

print(data_raw)