class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, time, data):
        self.data["data"] = data
        self.data["time"] =  time
        print(
            f"Received {len(data)} point"
        )

    def clear_data(self):
        self.data = {}
        print("Data cleared!!")

import numpy as np

sensor1 = Sensor(
    name="sensor1",
    location="Haldia",
    record_date="2023-01-09"
)
print(sensor1.name, sensor1.location, sensor1.record_date)

data = np.random.randint(-10, 10, 10)

time = np.arange(10)




sensor1.add_data(
    time=time,
    data=data
)

print(sensor1.data)

print(" -------------------------------- ")
class Accelerometer(Sensor):
    def show_sensor_type(self):
        print(f"I am an {self.name}")

acc = Accelerometer(
    "accelerometer",
    "Haldia",
    "2023-01-09"
)

acc.show_sensor_type()

data = np.random.randint(-10, 10, 10)
time = np.arange(10)
acc.add_data(data=data, time=time)
print(acc.data)
class Gyro(Accelerometer):
    def show_sensor_type(self):
        print(f"This is {self.name} and location is {self.location}")

gyro_data=np.random.randint(-15,15,10)
gyro_time=np.arange(10)

gyro =Gyro(
    name="Gyroscope",
    location="kolkata",
    record_date="2023-01-10"
)
gyro.add_data(time=gyro_time,data=gyro_data)

acc.show_sensor_type()
gyro.show_sensor_type()
class Gps(Sensor):
    def __init__(self, name, location, record_date,brand):
        super().__init__(name, location, record_date)
        self.brand=brand
        
gps=Gps(
    name="Gps",
    location="Chenni",
    record_date="2023-01-10",
    brand="espressif"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)