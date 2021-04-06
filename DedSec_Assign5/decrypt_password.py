from pyfinite import ffield
from brute_force_search import Add,Multiply,Expo,addVectors,scalarMultiplication,LinearTransformation

Multiplication_matrix = [[100, 122, 6, 10, 58, 9, 104, 13],
                        [0, 56, 121, 97, 14, 76, 30, 91],
                        [0, 0, 40, 77, 78, 114, 98, 54], 
                        [0, 0, 0, 50, 10, 116, 92, 58], 
                        [0, 0, 0, 0, 16, 92, 104, 113], 
                        [0, 0, 0, 0, 0, 87, 44, 17], 
                        [0, 0, 0, 0, 0, 0, 14, 37], 
                        [0, 0, 0, 0, 0, 0, 0, 103]]

Exponent_matrix = [85, 52, 38, 72, 116, 38, 66, 50]

mapdict = {
    '0000': 'f',
    '0001': 'g',
    '0010': 'h',
    '0011': 'i',
    '0100': 'j',
    '0101': 'k',
    '0110': 'l',
    '0111': 'm',
    '1000': 'n',
    '1001': 'o',
    '1010': 'p',
    '1011': 'q',
    '1100': 'r',
    '1101': 's',
    '1110': 't',
    '1111': 'u'
}

exp_cache = [[-1]*128 for i in range(128)]

F = ffield.FField(7) #Create finite field GF(128)


#Convert hex values to characters
def hex_to_char(st):
    char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
    return char
#To convert bytes to characters
def byte_to_char(b):
    num = '{:0>8}'.format(format(b,"b"))
    a = mapdict[num[0:4]], mapdict[num[4:8]]
    return a[0]+a[1]


def EAEAE (plaintext, mult_mat, exp_mat):
    plaintext = [ord(c) for c in plaintext]
    Output = [[0 for j in range (8)] for i in range(8)]
    for ind, elem in enumerate(plaintext):
        Output[0][ind] = Expo(elem, exp_mat[ind])

    Output[1] = LinearTransformation(mult_mat, Output[0])

    for ind, elem in enumerate(Output[1]):
        Output[2][ind] = Expo(elem, exp_mat[ind])

    Output[3] = LinearTransformation(mult_mat, Output[2])

    for ind, elem in enumerate(Output[3]):
        Output[4][ind] = Expo(elem, exp_mat[ind])
    return Output[4]



#It takes 16 charcters and return list of corresponding hex values
def string_to_byte(c):
    plainText = ""
    for i in range(0, len(c), 2):
        plainText += hex_to_char(c[i:i+2])
    return plainText
    
def DecryptPassword(password):
    passw = string_to_byte(password)
    op = ""
    for ind in range(8):
        for ans in range(128):
            inp = op + byte_to_char(ans)+(16-len(op)-2)*'f'
            if ord(passw[ind]) == EAEAE(string_to_byte(inp), Multiplication_matrix, Exponent_matrix)[ind]:
                op += byte_to_char(ans)
                break
    return op



print(string_to_byte(DecryptPassword("ktirlqhtlqijmmhq"))+string_to_byte(DecryptPassword("mgkplijngrluiqlq")))