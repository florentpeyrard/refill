from pyb import I2C
import ustruct
import utime

READOUT__AVERAGING_SAMPLE_PERIOD = 0x010A
SYSALS__ANALOGUE_GAIN = 0x003F
SYSRANGE__VHV_REPEAT_RATE = 0x0031
SYSALS__INTEGRATION_PERIOD = 0x0040
SYSRANGE__VHV_RECALIBRATE = 0x002E
SYSRANGE__INTERMEASUREMENT_PERIOD = 0x001B
SYSALS__INTERMEASUREMENT_PERIOD = 0x003E
SYSTEM__INTERRUPT_CONFIG_GPIO = 0x0014
SYSRANGE__MAX_CONVERGENCE_TIME = 0x001C
INTERLEAVED_MODE__ENABLE = 0x02A3
SYSRANGE__START = 0x0018
RESULT__RANGE_VAL = 0x0062
SYSTEM__INTERRUPT_CLEAR = 0x0015
SYSTEM__FRESH_OUT_OF_RESET = 0x0016

SYSRANGE__PART_TO_PART_RANGE_OFFSET = 0x024
SYSRANGE__CROSSTALK_VALID_HEIGHT = 0x021 
RESULT__INTERRUPT_STATUS_GPIO = 0x04F

SYSRANGE_INTERMEASUREMENT_PERIOD = 0x01B
SYSTEM_MODE_GPIO1 = 0x011
SYSRANGE_THRESH_LOW = 0x01A
SYSTEM_GROUPED_PARAMETER_HOLD    =     0x017


print('loading VL6180X2')
i2c = I2C(1, I2C.MASTER, baudrate=400000)

#i2c.mem_write(, 0x29, SYSRANGE__PART_TO_PART_RANGE_OFFSET, timeout=1000, addr_size=16)
#data = i2c.mem_read(1, 0x29, SYSRANGE__PART_TO_PART_RANGE_OFFSET, timeout=1000, addr_size=16)
#ptp_offset = ustruct.unpack("<h", data)[0]

i2c.mem_write(1, 0x29, 0x0207, timeout=1000, addr_size=16)
i2c.mem_write(1, 0x29, 0x0208, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, 0x0096, timeout=1000, addr_size=16)

#range  1x:253 2x:127 3x84
i2c.mem_write(253, 0x29, 0x097, timeout=1000, addr_size=16)
#i2c.mem_write(ptp_offset*3, 0x29, SYSRANGE__PART_TO_PART_RANGE_OFFSET, timeout=1000, addr_size=16)
#i2c.mem_write(20*3, 0x29, SYSRANGE__CROSSTALK_VALID_HEIGHT, timeout=1000, addr_size=16)

i2c.mem_write(0, 0x29, 0x00E3, timeout=1000, addr_size=16)
i2c.mem_write(4, 0x29, 0x00E4, timeout=1000, addr_size=16)
i2c.mem_write(2, 0x29, 0x00E5, timeout=1000, addr_size=16)
i2c.mem_write(1, 0x29, 0x00E6, timeout=1000, addr_size=16)
i2c.mem_write(3, 0x29, 0x00E7, timeout=1000, addr_size=16)
i2c.mem_write(2, 0x29, 0x00F5, timeout=1000, addr_size=16)
i2c.mem_write(5, 0x29, 0x00D9, timeout=1000, addr_size=16)
i2c.mem_write(206, 0x29, 0x00DB, timeout=1000, addr_size=16)
i2c.mem_write(3, 0x29, 0x00DC, timeout=1000, addr_size=16)
i2c.mem_write(248, 0x29, 0x00DD, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, 0x009F, timeout=1000, addr_size=16)
i2c.mem_write(60, 0x29, 0x00A3, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, 0x00B7, timeout=1000, addr_size=16)
i2c.mem_write(60, 0x29, 0x00BB, timeout=1000, addr_size=16)
i2c.mem_write(9, 0x29, 0x00B2, timeout=1000, addr_size=16)
i2c.mem_write(9, 0x29, 0x00CA, timeout=1000, addr_size=16)
i2c.mem_write(1, 0x29, 0x0198, timeout=1000, addr_size=16)
i2c.mem_write(23, 0x29, 0x01B0, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, 0x01AD, timeout=1000, addr_size=16)
i2c.mem_write(5, 0x29, 0x00FF, timeout=1000, addr_size=16)
i2c.mem_write(5, 0x29, 0x0100, timeout=1000, addr_size=16)
i2c.mem_write(5, 0x29, 0x0199, timeout=1000, addr_size=16)
i2c.mem_write(27, 0x29, 0x01A6, timeout=1000, addr_size=16)
i2c.mem_write(62, 0x29, 0x01AC, timeout=1000, addr_size=16)
i2c.mem_write(31, 0x29, 0x01A7, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, 0x0030, timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, SYSTEM__FRESH_OUT_OF_RESET, timeout=1000, addr_size=16)

#    #default config
i2c.mem_write(48, 0x29, READOUT__AVERAGING_SAMPLE_PERIOD, timeout=1000, addr_size=16)
i2c.mem_write(70, 0x29, SYSALS__ANALOGUE_GAIN, timeout=1000, addr_size=16)
i2c.mem_write(255, 0x29, SYSRANGE__VHV_REPEAT_RATE, timeout=1000, addr_size=16)
i2c.mem_write(99, 0x29, SYSALS__INTEGRATION_PERIOD, timeout=1000, addr_size=16)
i2c.mem_write(1, 0x29, SYSRANGE__VHV_RECALIBRATE , timeout=1000, addr_size=16)
i2c.mem_write(9, 0x29, SYSRANGE__INTERMEASUREMENT_PERIOD , timeout=1000, addr_size=16)
i2c.mem_write(49, 0x29, SYSALS__INTERMEASUREMENT_PERIOD  , timeout=1000, addr_size=16)
i2c.mem_write(36, 0x29, SYSTEM__INTERRUPT_CONFIG_GPIO   , timeout=1000, addr_size=16)
i2c.mem_write(49, 0x29, SYSRANGE__MAX_CONVERGENCE_TIME    , timeout=1000, addr_size=16)
i2c.mem_write(0, 0x29, INTERLEAVED_MODE__ENABLE     , timeout=1000, addr_size=16)  

#apply scaling on part-to-part offset
#data = i2c.mem_read(1, 0x29, SYSRANGE__PART_TO_PART_RANGE_OFFSET, timeout=1000, addr_size=16)
#base_offset = ustruct.unpack("<h", data)[0]
#ptp_offset = base_offset // 1
#print("ptp_offset"+str(ptp_offset))
#print(type(ptp_offset))
#i2c.mem_write(ptp_offset, 0x29, SYSRANGE__PART_TO_PART_RANGE_OFFSET, timeout=1000, addr_size=16)

#apply scaling on CrossTalkValidHeight
#i2c.mem_write(40, 0x29, SYSRANGE__CROSSTALK_VALID_HEIGHT, timeout=1000, addr_size=16)

def single_range_read():
    i2c.mem_write(1, 0x29, SYSTEM__INTERRUPT_CLEAR, timeout=1000, addr_size=16)
    #400 us delay
    #WaitDeviceBooted or 1 ms
    #InitData
    #Prepare
    #RangePollMeasurement
    print('readiness : '+str(i2c.is_ready(0x29)))
    #single range read
    i2c.mem_write(1, 0x29, SYSRANGE__START, timeout=1000, addr_size=16)
    #status = i2c.mem_read(1, 0x29, 77)
    #print(status)
    i = 0
    while (1):
        utime.sleep_ms(1)
        data = i2c.mem_read(1, 0x29, RESULT__INTERRUPT_STATUS_GPIO, timeout=1000, addr_size=16)
        status = ustruct.unpack("<h", data)[0]
        if (status & 0x04) == 0x04:
            data = i2c.mem_read(1, 0x29, RESULT__RANGE_VAL, timeout=1000, addr_size=16)
            readrange = ustruct.unpack("<h", data)[0]
            print('{:d}'.format(readrange))
            i2c.mem_write(1, 0x29, SYSTEM__INTERRUPT_CLEAR, timeout=1000, addr_size=16)
            break
        i+=1
        print('i='+str(i))
        if i>10:
            timedout = True
            print('timed out')
            break

def interrupt_range_read():
    i2c.mem_write(100, 0x29, SYSRANGE_INTERMEASUREMENT_PERIOD, timeout=1000, addr_size=16)
    
    #GPIO1 : interruptions ON, active high
    i2c.mem_write(48, 0x29, SYSTEM_MODE_GPIO1, timeout=1000, addr_size=16)
    
    #interrupt when range < low threshold
    i2c.mem_write(1, 0x29, SYSTEM_INTERRUPT_CONFIG_GPIO, timeout=1000, addr_size=16)
    
    #safe writing using grouped parameter hold
    i2c.mem_write(1, 0x29, SYSTEM_GROUPED_PARAMETER_HOLD, timeout=1000, addr_size=16)
    i2c.mem_write(254, 0x29, SYSRANGE_THRESH_LOW, timeout=1000, addr_size=16)
    i2c.mem_write(0, 0x29, SYSTEM_GROUPED_PARAMETER_HOLD, timeout=1000, addr_size=16)
    
    i2c.mem_write(3, 0x29, SYSRANGE__START, timeout=1000, addr_size=16)
    
    
