def move_zeros(lst):
    arr=[]
    z=0
    for i in lst:
        if i!=0:
            arr.append(i)
        else:
            z+=1
    for i in range(z):
        arr.append(0)
    return arr
