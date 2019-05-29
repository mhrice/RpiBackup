import VL53L1X
import time

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # Initialise the i2c bus and configure the sensor
tof.change_address(0x30)
tof.close()
#tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
#for i in range(100):
    #distance_in_mm = tof.get_distance() # Grab the range in mm
    #print(distance_in_mm)
    #time.sleep(1)
    
#tof.stop_ranging() # Stop ranging
#tof.close()
