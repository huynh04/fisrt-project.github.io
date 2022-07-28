def huynh(x):
    if x==0 or x==1:
        return x
    elif x==-1:
        return 0
    else:
        return huynh(x-1)+huynh(x-2)

for i in range(10):
    print(huynh(i), end=",")               
