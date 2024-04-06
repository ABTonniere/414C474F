string=input()
n=int(input())
string_out=""
if(n>0):
    for i in range(0, len(string), n):
        if i % (2*n) == 0:
            string_out += string[i:i+n]
        else:
            string_out += string[i:i+n][::-1]
        if(i+n<len(string)):
            string_out += "\n"
    print(string_out)
else:
    print(string)
