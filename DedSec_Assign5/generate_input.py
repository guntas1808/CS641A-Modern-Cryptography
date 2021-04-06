map = {}
for i in range(16):
    num = '{0:04b}'.format(i)
    # print(num)
    decimalvalue = int(num, base=2)
    map[num] = chr(ord('f')+decimalvalue)
# print(map)

file = open("inputs.txt","w+")
for i in range(8):
    for j in range(128):
        j_bin = '{0:08b}'.format(j)
        input = 'ff'*i + map[j_bin[:4]] + map[j_bin[4:]] + 'ff'*(8-i-1)
        file.write(input)
        file.write(" ")
    file.write("\n")
file.close()