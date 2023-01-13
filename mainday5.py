from sensorsday5 import Accelerometer,Gyro,Gps
import numpy as np
time=np.arange(10)
acc = Accelerometer(
   name= "accelerometer",
   location= "Haldia",
   record_date= "2023-01-09"
)
gyro =Gyro(
    name="Gyroscope",
    location="kolkata",
    record_date="2023-01-10"
)
gps=Gps(
    name="Gps",
    location="Chennai",
    record_date="2023-01-10",
    brand="espressif"
)
acc_data=np.random.randint(-10,10,10)
gyro_data=np.random.randint(-15,15,10)
gps_data=np.random.randint(-12,12,12)
print(acc.name)
print(acc.location)
print(acc.record_date)
acc.add_data(data=acc_data,time=time)

print(gyro.name)
print(gyro.location)
print(gyro.record_date)
gyro.add_data(data=gyro_data,time=time)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)
gps.add_data(data=gps_data,time=time)