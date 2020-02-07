def decipher(key, txt):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    key_ = [x for _, x in sorted(zip(key,alph))]
    txt_=""
    for i in range(len(txt)):
        if(ord('a')<=ord(txt[i]) and ord(txt[i])<= ord('z')):
            txt_+=key_[ord(txt[i])-ord('a')]
        elif(ord('A')<=ord(txt[i]) and ord(txt[i])<= ord('Z')):
            txt_+=key_[ord(txt[i])-ord('A')]
        else:
            txt_+=txt[i]
    return txt_

cipher_text = input()
frequency = list()
alph = list()
for i in range(26):
    frequency.append(0)
    alph.append(chr(ord('a')+i))

total_count = 1
#print(ord(cipher_text[0]))
#print(type(cipher_text[0]))

for i in range(len(cipher_text)):
    if(ord('a')<=ord(cipher_text[i]) and ord(cipher_text[i])<= ord('z')):
        total_count = total_count +1
        frequency[ord(cipher_text[i]) - ord('a')] = frequency[ord(cipher_text[i]) - ord('a')] + 1

    if(ord('A')<=ord(cipher_text[i]) and ord(cipher_text[i])<= ord('Z')):
        total_count = total_count + 1
        frequency[ord(cipher_text[i]) - ord('A')] = frequency[ord(cipher_text[i]) - ord('A')] + 1

for i in range(26):
    frequency[i] = (frequency[i]/total_count) * 100

alph_ = [x for _, x in sorted(zip(frequency,alph), reverse=True)]
frequency.sort(reverse=True)

for i in range(26):
    print((alph_[i]) + ": " + str(frequency[i]))

stand_alph = ['e','t','a','o','i','n','s','h','r','d','l','u','c','m','w','f','g','y','p','b','v','k','j','x','q','z']
alph_key = [x for _, x in sorted(zip(stand_alph,alph_))]

print("Possible key can be: ",*alph_key, sep="")

while(1):
    key = input("Enter Key to Decrypt:- abcdefghijklmnopqrstuvwxyz=")
    print(decipher(key, cipher_text))