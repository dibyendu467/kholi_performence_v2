# class SuperHero():
#     def __init__(self,name,superpower):
#         self.name=name
#         self.superpower=superpower
#     def get_superpower(self):
#         print(f"i am {self.name} and my power is {self.superpower}")
# ironMan= SuperHero(
#     name="iron man",
#     superpower="suit"
# )
# ironMan.get_superpower()

# thor=SuperHero(
#     name="thor",
#     superpower="thunder"
# )
# thor.get_superpower()


# inheritance ..............................................................................
class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}
        def add_data(self,data,time):
            self.data["data"]=data
            self.data["time"]=time
            print("Data points added successfully")
        def clear_data(self):
            self.data={}
            print("Data remove successfully")


import numpy as  np

sensor1=Sensor(
    name="Sensor1",
    location="haldia",
    record_date="2023-01-09"
)
data=np.random.randint(-10,10,10)
time=np.arange(10)
sensor1.add_data(
    data=data,
    time=time
)
print(sensor1.data)

class Accelerometer(Sensor):
    def show_sensor_type(self):
        print("this is {self.name}")
        acc=np.random.randint(-10,10,10)

        acc=Accelerometer(
            name="Accelerometer",
            location="haldia",
            record_date="2023-01-09"
        )
        acc.add_data(
            data=acc_data,
            time=acc_time
        )
        print()