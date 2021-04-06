#I need to make a key for each sbox
def sbox(s_input, i):
  s_out = ""
  S = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]



  row = int(s_input[0]+s_input[5] , base =2)
  column = int(s_input[1]+s_input[2]+s_input[3]+s_input[4] , base =2)
  s_out = '{0:04b}'.format(S[i][row][column])

  return s_out

def expand(text):
  temp = ""
  EXPANSION_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
  for x in EXPANSION_TABLE :
    temp += text[x-1]
  return temp

def in_perm(text):
    final = ""
    perm = [16,7,20,21,
        29,12,28,17,
        1,15,23,26,
        5,18,31,10,
        2,8,24,14,
        32,27,3,9,
        19,13,30,6,
        22,11,4,25]
    for x in perm:
        final += text[x-1]
    return final

def inv_in_perm(text):
    final = ""
    inv_perm = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]
    for x in inv_perm:
        final += text[x-1]
    
    return final

def permutation(plain_text):
  p = ""
  IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
  for x in IP :
    p += plain_text[x-1]
  return p


def inv_per(text):
  final = ""
  IP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
  for x in IP:
    final += text[x-1]
  return final


def last_perm(text):
    final = ""
    ipinv = [8,40,16,48,24,56,32,64,
         7,39,15,47,23,55,31,63,
         6,38,14,46,22,54,30,62,
         5,37,13,45,21,53,29,61,
         4,36,12,44,20,52,28,60,
         3,35,11,43,19,51,27,59,
         2,34,10,42,18,50,26,58,
         1,33,9,41,17,49,25,57]

    for x in ipinv:
        final += text[x-1]
    return final


def last_perm_inv(text):
    final = ""
    ipinvinv = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8]
    for x in ipinvinv:
        final += text[x-1]
    return final


def hex2bin(text):
    final = ""
    for i in range(16):
        final += '{0:04b}'.format(int(text[i], base = 16))
    return final

def hex2bin8(text):
        final = ""
        for i in range(8):
            final += '{0:04b}'.format(int(text[i], base = 16))
        return final


def bin2hex(text):
    final = ""
    for i in range(16):
        final += '{0:01x}'.format(int(text[4*i:4*i+4], base = 2))
    return final


def decode(text):
    final = ""
    for i in range(16):
        final += '{0:01x}'.format(ord(text[i]) - ord('f'))
    return final

def inv_per_func(text):
    temp = ""
    inv = [9,17,23,31,13,28,2,18,24,16,30,6,26,20,10,1,8,14,25,3,4,29,11,19,32,12,22,7,5,27,15,21]
    for x in inv:
        temp += text[x-1]
    return temp

#After initial permutation
char = "1234567800000000"

P = ['0000000000000000', '1100000000000000', '0000000000000001', '0011000000000000', '1111000000000000','1010100000000000']
P_star = ['0044140155110500', '1144140155110500', '0044140155110501', '0055140155110500', '1155140155110500','1054040155110500']
Pxor = '0044140155110500'


C_temp = ['gjuqtmorlfhoujmf','kjqnsiffinptnmgs','fkpqttrpnggspfhk','kfrpqigsmohunkhk','gktroljolntspknr','fkttsiorljpoumif']
C_star_temp = ['mogmqlkjjifqmokp','pnlssljojtkqhtif','htoiphfhlilihnfq','lnllqmksjufskpkq','tomrrlsjgtgnlrqj','ugfuhhjrnqisfoho']

C = []
C_star = []
C_xor = []
for x in C_temp:
    C.append(bin2hex(last_perm_inv(hex2bin(decode(x)))))
for x in C_star_temp:
    C_star.append(bin2hex(last_perm_inv(hex2bin(decode(x)))))
for i in range(6):
    temp = ""
    for j in range(16):
        temp += '{0:01x}'.format(int(C[i][j], base = 16) ^ int(C_star[i][j], base = 16))
    
    C_xor.append(temp)
L_0_hex = char[:8]

#3rd round xor output
xor_output = []
for x in C_xor:
    temp = ""
    for i in range(8):
        temp += '{0:01x}'.format(int(x[i], base = 16) ^ int(L_0_hex[i], base = 16))
    
    xor_output.append(temp)


xor_outp_remperm = []
for i in range(6):
    xor_outp_remperm.append(inv_in_perm(hex2bin8(xor_output[i])))
print(xor_outp_remperm)
print("\n")

#Calculate inputs
inp_exp = []
inp_exp_star = []

for i in range(6):
    inp_exp.append(expand(hex2bin8(C[i][8:])))
    inp_exp_star.append(expand(hex2bin8(C_star[i][8:])))

keys = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(8): # For each sbox
    for key in range(64):
        flag = 1
        for x in range(3):
            inp_final = '{0:06b}'.format(int(inp_exp[x][6*i:6*i+6], base = 2) ^ key)
            inp_star_final = '{0:06b}'.format(int(inp_exp_star[x][6*i:6*i+6], base = 2) ^ key)

            out_guess = sbox(inp_final,i)
            out_star_guess = sbox(inp_star_final,i)

            if(int(xor_outp_remperm[x][4*i:4*i+4], base = 2) != int(out_guess, base = 2) ^ int(out_star_guess, base = 2)):
                flag = -1
                break 

        if flag == 1:
            if keys[i] != i+1:
                print("More than one key for " + str(i+2))
            keys[i] = key

print(keys)

bin_42 = ""
for i in range(8):
    bin_42 += '{0:06b}'.format(keys[i])

print(bin_42)
