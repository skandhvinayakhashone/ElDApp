import time
import smbus
import math
import os

#I2C addresses
add= 0x4F
bus=smbus.SMBus(1)

#DtoA channel select
ch0= 0x00
ch1= 0x01
ch2= 0x02
ch3= 0x03

def readanalog(add):
    analog=bus.read_byte(add)
    return analog
   
def writedtoa(add,value):
    bus.write_byte_data (add, 0x44, value)

total_power=0

start=time.time()
end=0

while True:

    writedtoa(add,0)
    an0= readanalog(add)
    an0 = readanalog(add)
    print "channel 0 raw AtoD = ", an0
    V = 3.3 * an0 / 256
    V = round (V, 3)
    print "channel 0 Voltage = ", (V)
    Curr = 80 * V/(0.33)
    Curr = Curr / 10           
    Curr = Curr / 1.414         
    Curr = round (Curr , 1)
    Power = Curr * 240 /1000
    Power = round (Power, 0)
    total_power += Power
    if (round(end-start,0)/3600) == 1:
        os.system("python3 block_creator.py "+str(total_power))
        start=time.time()
    time.sleep(1)
    end=time.time()