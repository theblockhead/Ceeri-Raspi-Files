import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import smbus
# Create an MPU9250 instance
time.sleep(1)
mpu = MPU9250(
    address_ak=AK8963_ADDRESS,
    address_mpu_master=MPU9050_ADDRESS_68,  # In case the MPU9250 is connected to another I2C device
    address_mpu_slave=None,
    bus=1,
    gfs=GFS_1000,
    afs=AFS_8G,
    mfs=AK8963_BIT_16,
    mode=AK8963_MODE_C100HZ)
# 
# # Configure the MPU9250
try:
    mpu.configure()
except:
    print("not configure")
    
try:
    while True:
        # Read the accelerometer, gyroscope, and magnetometer values
        accel_data_list = mpu.readAccelerometerMaster()
        key_list = ['x','y','z']
        accel_data = {}
        for k,v in zip(key_list, accel_data_list):
            accel_data[k]= v*10.0
            
        gyro_data_list = mpu.readGyroscopeMaster()
        
        key_list = ['x','y','z']
        gyro_data = {}
        for k,v in zip(key_list, gyro_data_list):
            gyro_data[k]= v
        
#         print("Temp : "+str(mpu.get_temp()))
#         print()

        print("Acc X : "+str(accel_data['x']))
        print("Acc Y : "+str(accel_data['y']))
        print("Acc Z : "+str(accel_data['z']))
        print()

        print("Gyro X : "+str(gyro_data['x']))
        print("Gyro Y : "+str(gyro_data['y']))
        print("Gyro Z : "+str(gyro_data['z']))
        print()
        print("-------------------------------")
        time.sleep(1)
    # Wait for 1 second before the next reading
except:
    print("not reading")





