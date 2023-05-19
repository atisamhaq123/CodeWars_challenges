def valid_braces(string):
    x = string
    z= ["(","{","[","}",")"]
    if x.count("(")!=x.count(")") or x.count("{")!=x.count("}") or x.count("[")!=x.count("]"):
        return False
    else:
        z=[]
        for i in x:
            if (i=="}" and not "{" in z) or (i==")" and not "(" in z) or (i=="]" and not "[" in z) :
                return False
            z.append(i)
        for i in range(len(x)):
            if x[i]=="(" and x[len(x)-i-1]!=")" or x[i]=="{" and x[len(x)-i-1]!="}" or x[i]=="[" and x[len(x)-i-1]!="]":
                if x[i]=="(" and x[i+1]!=")" or x[i]=="{" and x[i+1]!="}" or x[i]=="[" and x[i+1]!="]":
                        return False
    return True
