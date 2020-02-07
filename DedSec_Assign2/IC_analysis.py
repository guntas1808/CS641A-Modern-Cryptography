def getIC(seq): 
    sum = 0
    for char in range(97, 123):
        freq = seq.count(chr(char)) + seq.count(chr(char-32))
        sum+= freq*(freq-1)
    IC = sum/(len(seq)*(len(seq)-1))

    return IC

seq = input("Enter the text:- ")
txt = ''.join(filter(lambda x: x not in [' ',':','!',',','.',';','_','"'] ,seq))
print("\n","The text has an Index of Coincidence of:- ",getIC(txt))