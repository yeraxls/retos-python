def mergeLists(list1, list2, m, n):
    if m > n:
        n,m = m,n
        list1,list2 = list2,list1
    p1 = m-1
    p2 = n-1
    for mp in range(m+n-1, -1, -1):
        if p1 < 0 or list2[p2] > list1[p1] or list1[p1] == None:
            list1[mp] = list2[p2]
            p2 -= 1
        else:
            list1[mp] = list1[p1]
            p1 -= 1
    return list1
    
list2 = [0,2,3,None,None,None,None]
n = 3
list1 = [-4,2,3,9]
m = 4
print(mergeLists(list1, list2,m,n))