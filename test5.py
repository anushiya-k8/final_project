from random import randint
ff=open("static/sb_name.txt","r")
sb_name=ff.read()
ff.close()
sb_name_array=sb_name.split(",")
na1=sb_name_array
sb_name_len=len(sb_name_array)
xn1=randint(1,sb_name_len)
xn2=xn1-1
name=na1[xn2]   
print(name)

'''ff=open("static/walletchain.json","r")
fj=ff.read()
ff.close()

fjj=fj.split('}')

nn=len(fjj)
nn2=nn-2
i=0
fsn=""
while i<nn-1:
    if i==nn2:
        
        fsn+=fjj[i]+"}"
    else:
        fsn+=fjj[i]+"},"
    i+=1
    
#fjj1='},'.join(fjj)

fj1="["+fsn+"]"
print(fj1)'''
    
