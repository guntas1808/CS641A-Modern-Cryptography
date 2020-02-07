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

seq = input("Enter the text:- ")
txt = ''.join(filter(lambda x: x not in [' ',':','!',',','.',';','_','"'] ,seq))
ICAnalysis(txt)