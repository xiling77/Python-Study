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
        