from pyfinite import ffield


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

#Convert hex values to characters
def hex_to_char(st):
    char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
    return char



#It takes 16 charcters and return list of corresponding hex values
def string_to_byte(c):
    plainText = ""
    for i in range(0, len(c), 2):
        plainText += hex_to_char(c[i:i+2])
    return plainText


exp_cache = [[-1]*128 for i in range(128)]

F = ffield.FField(7)

def Add (n1, n2):
    return int(n1) ^ int(n2)

def Multiply (n1, n2):
    return F.Multiply(n1, n2)

def Expo (no, power):
    if exp_cache[no][power] != -1:
        return exp_cache[no][power]

    result = 0
    if power == 0:
        result = 1
    elif power == 1:
        result = no
    elif power%2 == 0:
        sqrt_no = Expo(no, power>>1)
        result = Multiply(sqrt_no, sqrt_no)
    else:
        sqrt_no = Expo(no, power>>1)
        result = Multiply(sqrt_no, sqrt_no)
        result = Multiply(no, result)

    exp_cache[no][power] = result
    return result

def addVectors (v1, v2):
    result = [0]*8
    for i, (e1, e2) in enumerate(zip(v1, v2)):
        result[i] = Add(e1, e2)
    return result

def scalarMultiplication (v, elem):
    result = [0]*8
    for i, e in enumerate(v):
        result[i] = Multiply(e, elem)
    return result

def LinearTransformation (mat, elist):
    result = [0]*8
    for row, elem in zip(mat, elist):
        result = addVectors(scalarMultiplication(row, elem), result)
    return result



exponent_mat = [[] for i in range(8)]                         #Contains list of values for 1X8 vectors

multiplication_mat = [[[] for i in range(8)] for j in range(8)]     #Contains all values for each index in matrix


input_file = open("inputs.txt", 'r')
output_file = open("outputs.txt", 'r')


for index, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    inputs = []
    outputs = []

    for i in iline.strip().split(" "):
        inputs.append(string_to_byte(i)[index])             #Converting input to corresponding hex values
    for i in oline.strip().split(" "):
        outputs.append(string_to_byte(i)[index])             #Converting output to corresponding hex values
        
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for inps, outs in zip(inputs, outputs):
                #We iterate over all possible values of ei and ajj to check if input maps to output
                if ord(outs) != Expo(Multiply(Expo(Multiply(Expo(ord(inps), i), j), i), j), i):
                    flag = False
                    break
            if flag:
                exponent_mat[index].append(i)             #If the values match then we add the exp and aii values to list of possible values 
                multiplication_mat[index][index].append(j)


input_file = open("inputs.txt", 'r')
output_file = open("outputs.txt", 'r')


for index, (iline, oline) in enumerate(zip(input_file.readlines(), output_file.readlines())):
    #Considering only first 6 pairs
    if index > 6 :
        break

    inputs = []
    outputs = []
    #Converting each input to corresponding hex values
    for i in iline.strip().split(" "):
        inputs.append(string_to_byte(i)[index]) 
    for i in oline.strip().split(" "):
        outputs.append(string_to_byte(i)[index+1])
    for i in range(1, 128):
        #We iterate over all possible pairs of exponents and diagonal values
        for p1, e1 in zip(exponent_mat[index+1], multiplication_mat[index+1][index+1]):
            for p2, e2 in zip(exponent_mat[index], multiplication_mat[index][index]):
                flag = True
                for inp, outp in zip(inputs, outputs):
                    #We substitute the pairs ad=nd iterate over all possible values of i
                    #this is done by forming virtual triangle (aii,aij,ajj)
                    if ord(outp) != Expo(Add(Multiply(Expo(Multiply(Expo(ord(inp), p2), e2), p2), i) ,Multiply(Expo(Multiply(Expo(ord(inp), p2), i), p1), e1)), p1):
                        flag = False
                        break
                if flag:
                    #If we find such value, then we can discard other possibilities and finalize the lists
                    exponent_mat[index+1] = [p1]
                    multiplication_mat[index+1][index+1] = [e1]
                    exponent_mat[index] = [p2]
                    multiplication_mat[index][index] = [e2]
                    multiplication_mat[index][index+1] = [i]    



for index in range(6):
    #As we have already found element next to diagonal thus skipping two elements every time
    of = index + 2
    
    exp_list = [e[0] for e in exponent_mat]
    lin_trans_list = [[0 for i in range(8)] for j in range(8)]

    for i in range(8):
        for j in range(8):
            lin_trans_list[i][j] = 0 if len(multiplication_mat[i][j]) == 0 else multiplication_mat[i][j][0]

    inp = open("inputs.txt", 'r')
    out = open("outputs.txt", 'r')

    for index, (iline, oline) in enumerate(zip(inp.readlines(), out.readlines())):
        if index > (7-of):
            continue
        inputs = [string_to_byte(msg) for msg in iline.strip().split(" ")]
        outputs = [string_to_byte(msg) for msg in oline.strip().split(" ")]
        #We iterate over all possible values of ai,j to find which one satisfies EAEAE = Output
        for i in range(1, 128):
            lin_trans_list[index][index+of] = i
            flag = True
            for inps, outs in zip(inputs, outputs):
                if EAEAE(inps, lin_trans_list, exp_list)[index+of] != ord(outs[index+of]):
                    flag = False
                    break
            if flag:
                multiplication_mat[index][index+of] = [i]
    inp.close()
    out.close()


#We fill all the empty [] elements with 0
lin_trans_list = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        lin_trans_list[i][j] = 0 if len(multiplication_mat[i][j]) == 0 else multiplication_mat[i][j][0]

print(lin_trans_list)        
print(exp_list)



