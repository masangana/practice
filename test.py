fp = open("corruption.txt")
checksum =[]
for i, line in enumerate(fp):
    #if i == 0:
    mylist = line.split("\t")
    res = [eval(i) for i in mylist]
    mymin=min(res)
    mymax=max(res)
    #print("min=", i ,mymin)
    #print("max=", i,mymax)
    diff=mymax-mymin
    #print(diff)
    checksum.append(diff)
    print(checksum)
    total=sum(checksum)
    print('total',total)
#print(mylist)
#print((mylist))
#print(max(mylist))

fp.close()