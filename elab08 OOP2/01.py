class Switch:
    def __init__ (self,name,status = False):
        self.name = name
        self.clname = name + ".copy"
        self.status = status
    def turn(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False
    def clone(self):
        return Switch(self.name+".copy",self.status)
    def __str__(self):
        st = ''
        if self.status == True:
            st = "on"
        else:
            st = "off"
        return f"switch({self.name}) is {st}"
    
class Light:
    def __init__(self,name,switch):
        self.name = name
        self.switch = switch
    def turn(self):
        if self.switch.status == True:
            self.switch.status = False
        else:
            self.switch.status = True
    def get_status(self):
        return self.switch.status
    def set_switch(self,new_switch):
        self.switch = new_switch
    def clone(self):
        return Light(self.name+".copy",self.switch.clone())
    def __str__(self):
        sta = ''
        if self.switch.status == True:
            sta = "on"
        else:
            sta = "off"
   
        return f"light({self.name}) with switch({self.switch.name}) is {sta}"