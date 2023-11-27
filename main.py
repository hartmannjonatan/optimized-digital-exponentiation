from Bit import Bit
from BinaryNumber import BinaryNumber


def square_4bits(x: BinaryNumber):
    v1 = BinaryNumber(bits=[x[0], Bit(False), x[0]*x[1], x[0]*x[2], x[0]*x[3], x[1]*x[3], x[2]*x[3]])
    v2 = BinaryNumber(bits=[Bit(False), Bit(False), x[1], Bit(False), Bit(not x[1])*x[2], x[1]*x[2], x[3]])

    sum = v1+v2

    return sum

def cube_4bits(x: BinaryNumber):
    m = '''34	234	1’24	1’24	123	13	12	13	13	12	1
0	4	134	14	3+14	1’24	14	14	0	0	0
0	124	0	23+43	24	0	23+13	2	0	0	0
'''

    return somar_matriz_vetores(m, x)

def fourth_power_4bits(x: BinaryNumber):

    m = '''234	1234	2’34	124	123	1’34	1’23	12’3+1’234	124’	14	123+13	0	0	0	1
0	34	24	34	12’34	1’234+12’34	13’4	13+14	23+13	12’3	2	0	0	0	0
0	0	12’34	14	23’4	23+34	23’4	23+124	23	234+134	0	0	0	0	0
0	0	4	0	34	23’4	3	123+134	234+134	234+134	0	0	0	0	0
'''

    return somar_matriz_vetores(m, x)
    
def cube_5bits(x: BinaryNumber):
    m = '''45	345	1’235	2345	1345	13’45+1345’	34+23	123	15	12	13	13	12	1
0	135	1’35	1’2’35+1235	124	1’24+125	25	24	13	14	14	0	0	0
0	5	245	145	23’45+2345’	35+15	24+14	1’25	1’24	15	2	0	0	0
0	0	0	345’	1’35+23’5	235	135	3+14	0	23+13	0	0	0	0
0	0	0	45+25	4+15	0	0	0	0	0	0	0	0	0
'''
    return somar_matriz_vetores(m, x)

def somar_matriz_vetores(matriz: str, x: BinaryNumber):
    sum = BinaryNumber(value='0')
    for v in matriz.splitlines():
        sum += vetor_to_binaryNumber(v, x)
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
        
def test_5bits():
    for i in range(0, 32):
        i_bin = bin(i)[2:].zfill(5)
        x = BinaryNumber(i_bin)
        res = cube_5bits(x).decimal
        assert res == i**3, f"Erro: {i}**3 = {res} (correto: {i**3})"

def vetor_to_binaryNumber(vetor_str: str, x: BinaryNumber):
    v = vetor_str.split('\t')
    bits = []
    for i, b in enumerate(v):
        bit = []
        aux = None
        op_or = False
        for j, b_in in enumerate(b):
            if "’" == b_in:
                bit[len(bit)-1] = Bit(not bit[len(bit)-1])
            elif "+" == b_in:
                bit_formado = Bit(True)
                for aux2 in bit:
                    bit_formado *= aux2
                aux = bit_formado
                bit = []
                op_or = True
            else:
                if "0" == b_in:
                    bit.append(Bit(False))
                else:
                    bit.append(x[int(b_in) -1])
        bit_formado = Bit(True)
        for aux2 in bit:
            bit_formado *= aux2

        if op_or:
            bit_formado += aux

        bits.append(bit_formado)
    bits.reverse()
    return BinaryNumber(bits=bits)

def matriz_to_stdLogicVector(matriz: str):
    vetores = ""
    count = 1
    for v in matriz.splitlines():
        vetor = f"v{count} <="
        for bits in v.split("\t"):
            inicio_termo = True
            vetor = f"{vetor}(("

            for b in bits:
                if b == "’":
                    aux = vetor[len(vetor)-5:len(vetor) -1]
                    vetor = f"{vetor[0:len(vetor)-5]}not({aux}) "
                elif b == '+':
                    vetor = f"{vetor}) or ("
                    close_brackets = True
                    inicio_termo = True
                elif b == '0':
                    vetor = f"{vetor}'0'"
                else:
                    if inicio_termo:
                        vetor = f"{vetor} x({int(b)-1}) "
                        inicio_termo = False
                    else:
                        vetor = f"{vetor}and x({int(b)-1}) "
            vetor = f"{vetor})) & "
        count += 1
        vetores = f"{vetores}{vetor[0:len(vetor)-3]};\n"

    return vetores[0:len(vetores)-1]

m = '''234	1234	2’34	124	123	1’34	1’23	12’3+1’234	124’	14	123+13	0	0	0	1
0	34	24	34	12’34	1’234+12’34	13’4	13+14	23+13	12’3	2	0	0	0	0
0	0	12’34	14	23’4	23+34	23’4	23+124	23	234+134	0	0	0	0	0
0	0	4	0	34	23’4	3	123+134	234+134	234+134	0	0	0	0	0
'''

#print(matriz_to_stdLogicVector(m))

# test()

test_5bits()
