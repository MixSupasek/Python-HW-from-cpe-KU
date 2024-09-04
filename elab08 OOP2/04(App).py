class Line:
    def __init__(self,x1,y1,x2,y2):
        self.start_point = Point(x1,y1)
        self.end_point = Point(x2,y2)
        self.slope = (y2-y1)/(x2-x1)
        self.y_intercept = y2 - self.slope*x2 #### x1 = 0 จุดตัดแกน Y
    def contains(self,x,y):
        if self.start_point.get_x() < self.end_point.get_x():
            if self.end_point.get_x() >= x and self.start_point.get_x() <= x:
                yn = self.slope*x + self.y_intercept
                if yn == y:
                    return True
                else:
                    return False
            else:
                return False
        elif self.start_point.get_x() > self.end_point.get_x():
            if self.end_point.get_x() >= x and self.start_point.get_x() <= x:
                yn = self.slope*x + self.y_intercept
                if yn == y:
                    return True
                else:
                    return False
            else:
                return False
    def get_distance(self):
        return ((self.start_point.get_x()-self.end_point.get_x())**2 + (self.start_point.get_y()-self.end_point.get_y())**2)**(1/2)
    def get_x1(self):
        return self.start_point.get_x()
    def get_y1(self):
        return self.start_point.get_y()
    def get_x2(self):
        return self.end_point.get_x()
    def get_y2(self):
        return self.end_point.get_y()
    def get_y(self,x):
        yn = self.slope*x + self.y_intercept
        if self.contains(x,yn):
            return self.slope*x + self.y_intercept
        elif not self.contains(x,yn):
            return -999.999
class Point:
  # Constuctor
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def is_on_x_axis(self):
    if self.__y == 0: return True
    else: return False

  def is_on_y_axis(self):
    if self.__x == 0: return True
    else: return False

  def translate(self, dist_x, dist_y):
    self.__x = self.__x + dist_x
    self.__y = self.__y + dist_y

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y

  def set_x(self, new_x):
    self.__x = new_x

  def set_y(self, new_y):
    self.__y = new_y

  def __str__(self):
    return f"({self.__x}, {self.__y})"

  def __eq__(self, other):
    return self.__x == other.__x and self.__y == other.__y
x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))
L1 = Line(x1,y1,x2,y2)
print(f"value of x1 on this line is {x1:.3f}")
print(f"value of x2 on this line is {x2:.3f}")
print(f"value of y1 on this line is {y1:.3f}")
print(f"value of y2 on this line is {y2:.3f}")
print("==========")
print("Check x and y are on this line ?")
cx = int(input("Enter x : "))
cy = int(input("Enter y : "))
if L1.contains(cx,cy):
    print(f"x = {cx:.3f} and y = {cy:.3f} are on this line")
else:
    print(f"x = {cx:.3f} and y = {cy:.3f} are not on this line")
    
print(f"Distance between startPoint and endPoint is {L1.get_distance():.3f}")
print("==========")
print("Find value of y that gives( x , y ) on this line")
fx = int(input("Enter x : "))
print(f"value of y is {L1.get_y(fx):.3f}")
if L1.contains(fx,L1.get_y(fx)):
    print(f"( x , y ) = ( {fx:.3f} , {L1.get_y(fx):.3f} ) on this line")
else:
    print(f"( x , y ) = ( {fx:.3f} , {L1.get_y(fx):.3f} ) is not on this line")
