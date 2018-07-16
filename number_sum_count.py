fir_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens=[0,3,6,6,5,5,5,7,6,6]
hundred=7
res=0
for i in range(1,1000):
    s='{0:03}'.format(i)
    base1=int(s[2])
    base2=int(s[1])
    base3=int(s[0])
    if i<20:
        res+=fir_19[i] # one to nineteen
    elif base3==0:
        res+=tens[base2]+fir_19[base1] #20 to 99
    elif base3!=0 and base1==0 and base2==0:
        res+=fir_19[base3]+hundred #100,200,....900
    else:
        if base2==0 or base2==1:
            res+=fir_19[base3]+hundred+3+fir_19[base2*10+base1]
        else:
            res+=fir_19[base3]+hundred+3+tens[base2]+fir_19[base1]
print(res+11)