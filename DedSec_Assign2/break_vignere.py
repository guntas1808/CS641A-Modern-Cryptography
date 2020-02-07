#Calculate the index of coincidence for a string
def getIC(seq): 
    sum = 0
    for char in range(97, 123):
        freq = seq.count(chr(char)) + seq.count(chr(char-32))
        sum+= freq*(freq-1)
    IC = sum/(len(seq)*(len(seq)-1))

    return IC

#IC Analysis 
def ICAnalysis(txt):
    print("KeyLength --------- I.C.")
    for keylen in range(1,31):
        avgIC = 0
        for i in range(1,keylen+1):
            seq=""
            for pos in range(i-1, len(txt), keylen):
                seq+=txt[pos]
            if(seq is not ""):
                avgIC+=getIC(seq)
        avgIC/=keylen
        print(keylen," --------- ",avgIC)
    return

#Shift a sequence given the key letter
def shift_seq(seq, shift):
    shif_seq=""
    for i in range(0,len(seq)):
        if((ord(seq[i])-shift)<97):shif_seq += chr(26+(ord(seq[i])-shift))
        else: shif_seq += chr(ord(seq[i])-shift)
    return shif_seq

#Calculate the Chi-Squared Statistic for a string
def ChiSq(seq):
    alpha_prob = [0.08167,0.01492,0.02202,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153, 0.01292,0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09356, 0.02758, 0.00978, 0.02560, 0.00150, 0.01994, 0.00077]
    expec_count = [p*len(seq) for p in alpha_prob] #expected count of alphabets
    count = list()
    for i in range(0,26):count.append(0)
    for char in range(97, 123):
        count[char-97] = seq.count(chr(char))
    ChiSq_val = 0
    for i in range(0,26):
        ChiSq_val+=((count[i]-expec_count[i])*(count[i]-expec_count[i]))/expec_count[i]
    
    return ChiSq_val

#Runs a Chi-Squared Statistic Analysis on the string
def ChiSq_Analysis(txt, keylen):
    print("The key is:-")
    for i in range(0,keylen):
            min_val=float('inf')
            corr_shift = 0
            seq=""
            for pos in range(i, len(txt), keylen):
                seq+=txt[pos]
            for shift in range(0,26):
                seq_ = shift_seq(seq, shift)
                val = ChiSq(seq_)
                if(val<min_val):
                    min_val = val
                    corr_shift = shift
            print(chr(corr_shift+97))
    return

if __name__ == "__main__":
    cipher_txt = input()
    purecipher_txt = ''.join(filter(lambda x: x not in [' ',':','!',',','.',';','_','"'] ,cipher_txt))

    print("IC test-------------")
    ICAnalysis(purecipher_txt)
    
    keylen = int(input("Enter the keylength? "))
    
    print("Chi Squared Analysis-------")
    ChiSq_Analysis(purecipher_txt,keylen)


    
