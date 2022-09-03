#Print prime numbers between 1-200 using for loop

for i in range(1,200):
    if i==1:
        print(i,'\n')
    else:
        for j in range(2,i):
            if ((i%j)==0):
                break
        else:
            print(i,'\n')
            
