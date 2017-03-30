import pyb
import gc  
import uos
import micropython
from lib.umqtt.robust import MQTTClient
from pyb import Pin, ExtInt
import VL6180X
micropython.alloc_emergency_exception_buf(100)
def freeRAMCheck(timer):
    free = gc.mem_free()
    if (int(free)<20000):
        print('low RAM')
        tim1.deinit()
tim1 = pyb.Timer(1,freq=0.5,callback=freeRAMCheck)
def freeDiskSpaceCheckCallback(timer):
    freeDiskSpaceCheck()
stats = bytearray(320)
def freeDiskSpaceCheck():
    #pyb.info()
    stats[0] = uos.statvfs("/flash")
    #pyb.info()
    #free = int(stats[0])*int(stats[3])
    #if (free<90000):
    #    print('low disk space')
    #    tim4.deinit()
    
def connect_mqtt(server="anmbfjfo981en.iot.us-west-2.amazonaws.com"):
    c = MQTTClient("refiller1", server,ssl=True,ssl_params={"/flash/tls/1e1e160a77-private.pem.key","/flash/tls/1e1e160a77-certificate.pem.crt","/flash/tls/CACertif.pem"})
    c.connect()
    print("Connected to %s, waiting for button presses" % server)


VL6180X.interrupt_range_read()
def onDectection:
    print('Detection')
ext = ExtInt(Pin('Y1'), ExtInt.IRQ_RISING, Pin.PULL_NONE, onDetection)
