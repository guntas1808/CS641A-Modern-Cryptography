from DES import gen_key, encrypt

def split_key(key_56):
  l,r=key_56[:28],key_56[28:]
  return l,r


def circular_shift(key,n):
  temp=""
  temp=key[n:]+key[:n]
  return temp


key_48bit = "000001000010000011000100000101000110000111001000"
key_56bts = ""
miss_bits = list() #positions
p_inv = [5, 24, 7, 16, 6, 10, 20, 18, 'x', 12, 3, 15, 23, 1, 9, 19, 2, 'x', 14, 22, 11, 'x', 13, 4, 'x', 17, 21, 8, 46, 31, 27, 48, 35, 41, 'x', 47, 28, 'x', 39, 32, 25, 44, 'x', 37, 34, 43, 29, 36, 38, 45, 33, 26, 42, 'x', 30, 40]

for t in p_inv:
    if t == 'x':
        key_56bts += '2'
    else:
        key_56bts += key_48bit[t-1]
# print(key_56bts)

left, right = split_key(key_56bts)
left = circular_shift(left, 22)
right = circular_shift(right, 22)
# print(left+right)
key_56bitl = list(left + right)

for i in range(56):
    if key_56bitl[i] == '2':
        miss_bits.append(i)

for i in range(2**8):
    temp = '{0:08b}'.format(i)
    for indx in range(8):
        key_56bitl[miss_bits[indx]] = temp[indx]
    key_56bts = ''.join(map(str, key_56bitl))
    subkeys = gen_key(key_56bts)

    if encrypt('1100000000000000', subkeys) == '6632b2640597e1c4':
        print("success\n" + key_56bts)
    