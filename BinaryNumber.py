from Bit import Bit


class BinaryNumber:
    def __init__(self, value: str = '0', value_decimal: int = None, bits: list = None):
        self.__value = []
        self.__string = ''
        if bits is None:
            if not value_decimal is None:
                value = bin(value_decimal)[2:]
            self.__string = value
            value = value[::-1]
            for digit in value:
                if digit == '1':
                    self.__value.append(Bit(True))
                elif digit == '0':
                    self.__value.append(Bit(False))
                else:
                    raise ValueError("BinaryNumber deve ter apenas '0' e '1' como valor.")
        else:
            for bit in bits[::-1]:
                self.__string = f"{self.__string}{str(bit)}"
            self.__value = bits
        
    def __str__(self) -> str:
        return self.__string
    
    def __getitem__(self, indice):
        return self.__value[indice]
    
    @property
    def decimal(self):
        return int(self.__string, 2)
    
    def __add__(self, other):
        return BinaryNumber(value_decimal=self.decimal + other.decimal)
    
    def __sub__(self, other):
        return BinaryNumber(value_decimal=self.decimal - other.decimal)