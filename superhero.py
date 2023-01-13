 #class SuperHeroes:
#     def _init_(self,name,superpower):
#         self.name = name
#         self.superpower = superpower

#     def _str_(self):
#         return f"I am {self.name} and my superpower is {self.superpower}"
    
# ironMan = SuperHeroes("Iron Man","billionaire")
# print(ironMan)

# thor=SuperHeroes("Thor","Thunder")
# print(thor)
#--------------------------------------------------------------------------------------------------------------


class Sensor():
    def _init_(self,name,location,record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data={}

    def add_data(self,data,time):
        self.data["data"] = data
        self.data["time"] = time
        print("Data points added successfully")

    def clear_data(self):
        self.data = {}
        print("Data cleared successfully")
import numpy as np
sensor1=Sensor(name="Sensor 1",location="Haldia",record_date="2023-01-09")

data=np.random.randint(-10,10,10)
time=np.arange(10)

sensor1.add_data(data,time)
print(sensor1.name,sensor1.data)

class Accelerometer(Sensor):
    def show_sensor_type(self):
        print("This is {}".format(self.name))

acc_data=np.random.randint(-20,5,10)
acc_time=np.arange(10)

acc=Accelerometer("Accelerometer",location="Haldia",record_date="2023-01-09")
acc.add_data(acc_data,acc_time)

print(acc.name,acc.data)