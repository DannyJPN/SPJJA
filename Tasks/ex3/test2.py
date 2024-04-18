def my_avg(*li):
    s = 0
    c = 0      
    for i in li:
        if type (i) == int or type(i) == float:
            s+=i
            c+=1
    return s/c




def divide(num,li):
    return list(map(lambda a:a//num,li))

def my_map(func,li):
    return [func(x) for x in li]

def calls(filename):
    lines = []
    with open(filename) as f:
         lines = [str(j).split(",") for j in f]
    
    return numbercounter(lines)

def numbercounter(li):
    cols = [[],[],[]]    
    for x in li:
        for ind in range(3):
            cols[ind].append(float(x[ind].strip()))
    priv = []
    publ = []
    for x in cols[1]:
        if x not in priv:
            priv.append(x)
    for x in cols[0]:
         if x not in publ and x not in priv:
            publ.append(x)  
    map(lambda a:str(int(a)),publ)
    map(lambda a:str(int(a)),priv)    

    privprices = [0,0]
    publprices = [0,0]
    for x in li:
        print(x[0])
        print(str(str(x[0]) in priv) + "\t"+ str(priv))
        print(str(str(x[0]) in publ) + "\t"+ str(publ))

        if x[0] in priv and x[1] == str(priv[0]):
            print("X0 "+ str(x[0])+"\tX1 " + str(x[1]) + "\t Matched cond1")
            privprices[0]+=1
        if x[0] in publ and x[1] == str(priv[0]):
            print("X0 "+ str(x[0])+"\tX1 " + str(x[1]) + "\t Matched cond2")
            publprices[0]+=1
        if x[0] in priv and x[1] == str(priv[1]):
            print("X0 "+ str(x[0])+"\tX1 " + str(x[1]) + "\t Matched cond3")
            privprices[1]+=1
        if x[0] in publ and x[1] == str(priv[1]):
            print("X0 "+ str(x[0])+"\tX1 " + str(x[1]) + "\t Matched cond4")
            publprices[1]+=1
        


    return [publprices,privprices]
   
l = [3,4,5,7,8,4,5,1,2]


print(my_avg(1,2,3))
print(divide(2,l))
print(list(map(lambda a:int(a/2),l)))
print(my_map(lambda a:int(a/2),l))
print(calls("calls.txt"))

