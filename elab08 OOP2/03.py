import math


class Cylinder:

    
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height


        """get_radius()"""
        
    def get_radius(self):
        return self.radius


        """get_height()"""
        
    def get_height(self):
        return self.height


        """set_radius()"""
        
    def set_radius(self,new_radius):
        self.radius = new_radius


        """set_height()"""
        
    def set_height(self,new_height):
        self.height = new_height


        """get_base_area()"""
        
    def get_base_area(self):
        return math.pi*self.radius**2


        """get_volume()"""
        
    def get_volume(self):
        return self.get_base_area()*self.height


        """__str__()"""
        
    def __str__(self):
        return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"

