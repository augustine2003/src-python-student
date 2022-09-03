#*args Concept

#Multiply numbers

def mul(arg1,*argv):
    product=1
    for arg in argv:
        product*=arg
    return product

print("Multiplying Numbers..\n")
print("Product from 1 to 10 is %d" % mul(1,2,3,4,5,6,7,8,9,10))

#Output will be 3628800

#**kwargs Concept

def pt(**kwargs):
    for keys,value in kwargs.items():
        print("%s : %s" % (keys,value))

pt(one='Roll',two='jump',three='spin')

#Output will be
#one : Roll
#two : jump
#three : spin

