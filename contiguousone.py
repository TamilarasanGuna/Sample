def LengthContiguousBinary(binstr):
    count=0
    m=0
    for i in range(len(binstr)):
        if(binstr[i]=='1'):
            count+=1
            if(m<count):
                m=count;
        else:
            count=0
    return m;
binstr=input()
print(LengthContiguousBinary(binstr))