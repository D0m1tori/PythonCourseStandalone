import copy
def check_analysis(**kwargs):
    Dict1 = {}
    Dict2 = {}
    for i in kwargs:
        s = 0
        for j in kwargs[i]:
            s+= kwargs[i][j]
            if(j in Dict2):
                Dict2[j] +=1
            else:
                Dict2[j] = 1
        Dict1[i] = s
    print("(\"",end="")
    for i in Dict1:
        if(Dict1[i] == max(Dict1.values())):
            a = i
            print(i,end="\", \"")
            break
    for i in Dict2:
        if(Dict2[i] == max(Dict2.values())):
            b = i
            print(i,end = "\")")
            break
    return a,b


#check_analysis(id123={"яблоко": 100, "банан": 50},
#id124={"банан": 50, "апельсин": 70},
#id125={"яблоко": 100, "апельсин": 70})