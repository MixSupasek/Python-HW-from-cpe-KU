class Radio:
    def __init__(self,mode = "FM",frequency = 87.5):
        self.mode = mode
        self.frequency = frequency
    def set_mode(self,mode):
        if self.mode == 'FM' and mode == 'AM':
            self.mode = mode
            self.frequency = 150
        elif self.mode == 'AM' and mode == 'FM':
            self.mode = mode
            self.frequency = 87.5
    
    def set_frequency(self,frequency):
        if self.mode == "FM":
            if frequency >= 87.5 and frequency <= 108:
                self.frequency = frequency
            else:
                pass
        elif self.mode == "AM":
            if frequency >= 150 and frequency <= 280:
                self.frequency = frequency
            else:
                pass
    def adjust_frequency(self,frequency):
        if self.mode == "FM":
            if (self.frequency+frequency) <= 108 and (self.frequency+frequency) >= 87.5:
                self.frequency += frequency
                return True
            else:
                return False
        elif self.mode == "AM":
            if (self.frequency+frequency) <= 280 and (self.frequency+frequency) >= 150:
                self.frequency += frequency
                return True
            else:
                return False
    def get_mode(self):
        return self.mode
    def get_frequency(self):
        return self.frequency
    def __str__(self):
        if self.mode == "FM":
            return f"{self.mode} Radio: {self.frequency:.1f} MHz"
        elif self.mode == "AM":
            return f"{self.mode} Radio: {self.frequency:.1f} kHz"