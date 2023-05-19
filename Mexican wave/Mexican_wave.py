def wave(people):
    x=people
    f=[]
    for i in range(len(x)):
        if x[i]!=" ":
            z=x[:i]+x[i].upper()+x[i+1:]
            f.append(z)
    return f
