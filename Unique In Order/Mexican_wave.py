def unique_in_order(iterable):
    new=[]
    if len(iterable)>0:
        for i in range(len(iterable)-1):
            if iterable[i]!=iterable[i+1]:
                new.append(iterable[i])
        new.append(iterable[len(iterable)-1])
        return new
    return new
