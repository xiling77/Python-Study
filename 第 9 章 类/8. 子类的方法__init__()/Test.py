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

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        


my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())


