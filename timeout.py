import timeit


def funk():
    #imp1 = input()
    #arr = input()
    #a = input()
    #b = input()
    
    arr = '1 5 3'
    a = '3 1'
    b = '5 7'
    
    arr = arr.split(' ')
    arr = [int(x) for x in arr]
    
    a = a.split(' ')
    a = [int(x) for x in a]
    
    b = b.split(' ')
    b = [int(x) for x in b]
    
    hap = 0
    
    for i in arr:
        if i in a:
            hap += 1
        elif i in b:
            hap -= 1
    
    #print(hap)


print(timeit.timeit('funk()', globals=globals()))