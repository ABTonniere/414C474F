string=input()
n=int(input())
string_out=""
str2=string.split(' ')
size=0
inv=False
invertor=""
releg=0
for elm in str2:
    if(size>=n):
        if(inv==True):
            string_out += " ".join(invertor.split(" ")[::-1])
            invertor=""
        inv=not inv
        size=0
        string_out += "\n"
    if(inv==False):
        
        if(releg==1):
            string_out += " "
            size+=1
            releg=0
        
        string_out += elm
        size+=len(elm)
        
        if(size>=n):
            releg=1
            if(size+1>=n):
                size+=1
        else:
            string_out += " "
            size+=1
        
        
    else:
        if(releg==1):
            invertor+=" "
            size+=1
            releg=0
        invertor+=str(elm[::-1])
        size+=len(elm)
        if(size>=n):
            releg=1
            if(size+1>=n):
                size+=1
        else:
            invertor += " "
            size+=1
    
print(string_out)