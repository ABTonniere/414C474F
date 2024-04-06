def if_number(x):
        if x.isdigit():
            return True
        else:
            return False

def preparator(equ):
    equ_split=[]
    equ_split_return=[]
    for elm in equ:
        for letter in elm:
            equ_split.append(letter)
        equ_split_return.append(equ_split)
        equ_split=[]
    return equ_split_return

def dictionnatitator(equ):
    dict={}
    
    for elm in equ:
        temp=1
        for i in range(len(elm)):
            if if_number(elm[i]):
                if(i==0):
                    temp=int(elm[i])
                else:
                    dict[elm[i-1]]+=int(elm[i])*temp
            else:
                if((elm[i] in dict.keys() )and (i+1 < len(elm)) and not (if_number(elm[i+1]))):
                    dict[elm[i]]+=temp
                elif((elm[i] in dict.keys() )and not (i+1 < len(elm))):
                    dict[elm[i]]+=temp
                elif (not (elm[i] in dict.keys() )) and (i+1 < len(elm)) and  (if_number(elm[i+1])):
                    dict[elm[i]]=0
                elif((elm[i] in dict.keys() )and (i+1 < len(elm)) and (if_number(elm[i+1]))):
                    pass
                elif (not (elm[i] in dict.keys() )) and (i+1 < len(elm)) and  not (if_number(elm[i+1])):
                    dict[elm[i]]=temp
                elif(not (elm[i] in dict.keys() )and not (i+1 < len(elm))):
                    dict[elm[i]]=temp
        
    return dict

def calculator(dict_base,dict_res):
    for key in dict_base.keys():
        if key in dict_res.keys():
            if dict_res[key]==dict_base[key]:
                continue
            else:
                return 0
        else:
            return 0
    return 1

equ_n=int(input())
for _ in range(equ_n):
    equ=input()
    equ=equ.replace(" ","")
    equ=equ.split("->")
    if(len(equ)>1):
        equ_base=equ[0]
        equ_res=equ[1]
        equ_base=equ_base.split("+")
        equ_res=equ_res.split("+")
        
        
        equ_base=preparator(equ_base)
        dict_base=dictionnatitator(equ_base)
        equ_res=preparator(equ_res)
        dict_res=dictionnatitator(equ_res)

        print(dict_base)
        print(dict_res)
        print(calculator(dict_base,dict_res))
    else:
        print(1)
    
#H2O -> H2 + O2
#2H2O -> 2H2 + O2
#C3H8 + O2 -> CO2 + H2O
#C3H