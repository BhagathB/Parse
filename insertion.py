import datetime
def insertion(l):
    for sliceend in range(len(l)):
        pos = sliceend
        while(pos>0 and l[pos] <l[pos-1]):
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos = pos-1
    return(l)

x = datetime.datetime.now().time().microsecond
print(insertion([7,5,9,2,11,0,20,200,234,2308,1024,1481,149815,1241,1453,22356745,374453246,4384747,1314,1526,12325,2735235,2372525,61452]))
y = datetime.datetime.now().time().microsecond
print(y-x)
