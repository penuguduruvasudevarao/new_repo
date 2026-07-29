from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self,radius):
        self.Area=3.14*radius**2
        print(self.Area)
class Square(Shape):
    def area(self,side):
        self.Area=side*4 
        print(self.Area)
c=Circle()
s=Square()
c.area(4)
s.area(4)