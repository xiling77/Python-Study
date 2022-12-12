class Dog():
    """小狗"""
    def __init__(self,name,age):
        """初始化name and age"""
        self.name = name
        self.age = age
     
    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title()+ " is now sitting.")
        
    def rool_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")
        

my_dog = Dog("whillie", 6)
    
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")