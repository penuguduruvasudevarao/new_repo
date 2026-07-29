class Circle:
    def draw(self):
        print("Drawing Circle")
class Square:
    def draw(self):
        print("Drawing square")
class Triangle:
    def draw(self):
        print("Drawing Triangle")

shapes=[Circle(),Square(),Triangle()]
for shape in shapes:
    print(shape.draw())