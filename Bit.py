class Bit:
    def __init__(self, value: bool):
        self.__value = 1 if value else 0
        self.__bool = value

    @property
    def value(self):
        return self.__value
    
    @property
    def bool(self):
        return self.__bool
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __add__(self, other):
        return Bit(self.bool or other.bool)
    
    def __mul__(self, other):
        return Bit(self.bool and other.bool)
    
    def __bool__(self):
        return self.bool