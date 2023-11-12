from Bit import Bit
from BinaryNumber import BinaryNumber


def square_4bits(x: BinaryNumber):
    v1 = BinaryNumber(bits=[x[0], Bit(False), x[0]*x[1], x[0]*x[2], x[0]*x[3], x[1]*x[3], x[2]*x[3]])
    v2 = BinaryNumber(bits=[Bit(False), Bit(False), x[1], Bit(False), Bit(not x[1])*x[2], x[1]*x[2], x[3]])

    sum = v1+v2

    return sum

def cube_4bits(x: BinaryNumber):
    v1 = BinaryNumber(bits=[x[0], x[0]*x[1], Bit(False), x[0]*x[3], x[0]*x[3], Bit(False), x[0]*x[2]*Bit(not x[3]), x[0]*Bit(not x[1])*x[3], x[0]*x[1]*x[3], x[1]*x[3], x[2]*x[3]])
    v2 = BinaryNumber(bits=[Bit(False), Bit(False), x[0]*x[1], x[1], x[0]*x[1]*x[2], x[0]*x[1]*x[2], x[0]*Bit(not x[1])*x[3], x[1]*x[2], x[0]*x[2]*x[3], x[3], Bit(False)])
    v3 = BinaryNumber(bits=[Bit(False), Bit(False), x[0]*x[1], x[0]*x[1], x[1]*x[2], x[0]*x[1]*x[3], x[2], Bit(not x[1])*x[2]*x[3], Bit(False), x[1]*x[2]*x[3], Bit(False)])

    sum = v1+v2+v3
    sum = sum - BinaryNumber(bits=[Bit(False), Bit(False), x[0]*x[2]])
    sum = sum - BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), x[1]*x[3]])

    return sum

def fourth_power_4bits(x: BinaryNumber):
    v1 = BinaryNumber(bits=[x[0], Bit(False), Bit(False), Bit(False), Bit(False), x[0]*x[1]*x[2], x[0]*x[1], x[0]*x[2], x[0]*x[1]*x[3], x[0]*x[1]*x[2], x[0]*x[3],  x[0]*x[1]*x[2]*x[3], x[0]*x[2]*x[3], x[1]*x[2]*x[3], x[2]*x[3]])
    v2 = BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), x[1], x[0]*x[3], x[0]*x[3], x[0]*x[1]*x[2], Bit(not x[0])*x[2], x[0]*Bit(not x[1])*x[2]*x[3], x[1]*x[2], x[1]*x[3], Bit(not x[1])*x[3], x[1]*x[3]])
    v3 = BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), x[0]*x[2]*x[3], x[0]*Bit(not x[1])*x[3], x[0]*x[3], Bit(False), x[1]*x[2]*x[3], x[0]*x[3], x[0]*x[1]*x[3]])
    v4 = BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), x[0]*x[2]*x[3], x[0]*x[2]*x[3], x[0]*Bit(not x[1])*x[3], x[0]*x[2]*x[3], x[0]*x[2], Bit(False), x[1]*x[2]*x[3]])

    sum = v1+v2+v3+v4

    sum = sum - BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), x[0]*x[2]])
    sum = sum - BinaryNumber(bits=[Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), Bit(False), x[1]*x[3]])

    return sum


def test():
    for i in range(0, 16):
        i_bin = bin(i)[2:].zfill(4)
        x = BinaryNumber(i_bin)
        res = square_4bits(x).decimal
        assert res == i**2, f"Erro: {i}**2 = {res} (correto: {i**2})"
        res = cube_4bits(x).decimal
        assert res == i**3, f"Erro: {i}**3 = {res} (correto: {i**3})"
        res = fourth_power_4bits(x).decimal
        assert res == i**4, f"Erro: {i}**4 = {res} (correto: {i**4})"

test()