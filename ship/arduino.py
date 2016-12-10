import serial
from .models import Department, Soldier, SingleRecord
import time
#import numpy



 # Takes ~2 secs to open the connection (non blocking), so made global
#ser = serial.Serial('/dev/ttyUSB1', 115200)
arduinoData = serial.Serial('com3', 115200)
while True:
    while arduinoData.inWaiting() == 0:
        pass # do nothing
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split(' ')
    tag_field_0 = dataArray[0]
    tag_field_1 = dataArray[1]
    tag_field_2 = dataArray[2]
    tag_field_3 = dataArray[3]
    record_for_db = SingleRecord(532,0 ,tag_field_0, tag_field_1, tag_field_2, tag_field_3)

    record_for_db.save()
    time.sleep(1) #to prevent DB flooding