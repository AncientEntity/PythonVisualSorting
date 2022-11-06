import random

unsorted = []
for i in range(1000):
    #unsorted.append(random.randint(0,9999999))
    unsorted.insert(min(len(unsorted),random.randint(0,i)),i)


def MergeSort(a,b=[]):
    #print("A:",a)
    #print("B:",b)
    if(len(b) == 0):
        return MergeSort(a[0:len(a)//2],a[len(a)//2:len(a)])
    else:
        c = a
        if(len(c) > 1):
            c = MergeSort(a[0:len(a)//2],a[len(a)//2:len(a)])
        d = b
        if(len(d) > 1):
            d = MergeSort(b[0:len(b)//2],b[len(b)//2:len(b)])
        print("C:",c)
        print("D:",d)
        for j in range(len(b)):
            i = 0
            while(i < len(c) and c[i] < d[j]):
                i += 1
            c.insert(i,d[j])
        return c

print(unsorted)
print(MergeSort(unsorted))
