class Car():
    """模拟汽车"""
    
    def __init__(self, make, model,year):
        """初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading +=miles

#####################################################################################

class Battery():
    """模拟电动车电瓶"""
    def __init__(self,battery_size = 70):
        """初始化"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

#####################################################################################

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        
        """每次创建一个ElectricCar类都会有一个Battery类被创建"""
        self.battery = Battery()    
        
#####################################################################################

my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


'''类Car-->类ElectricCar           父类子类           '''
'''类Battery-->类ElectricCar       实例当作类的属性   '''
