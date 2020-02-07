from itertools import permutations

#Print all the permutations of the string txt with block length=keylen 
def getPerm(txt, keylen):
    count = 0
    perm = list(permutations([x for x in range(1,keylen+1)])) #All possible permutations (= keylen!)
    for key in perm:   
        txt_ = ""
        for block in range(0, len(txt), keylen):
            for pos in range(keylen):
                txt_ += txt[block+key[pos]-1]
        
        # if(txt_[22] is not txt_[21] and txt_[len(txt_)-5] is txt_[len(txt_)-6]):  #"ff" should not occur and last word should be password
        print(txt_,"\n")
        print(key)
        print("------------------------------------")
        count+=1
    
    print(count, "Possible Permutations")

    return 


#Input text
cipher_txt = input("Input string - ")
#Remove pnctuations and spaces
purecipher_txt = ''.join(filter(lambda x: x not in [' ',':','!',',','.',';','_','"'] ,cipher_txt))
#Permutation Keylength
keylen = int(input("keylength - "))


getPerm(purecipher_txt,keylen)