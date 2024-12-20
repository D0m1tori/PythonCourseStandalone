import copy
def apply_multiple(data, func1, func2):
    data1 = data.copy()
    for i in range(len(data1)):
        data1[i]= func1(data1[i])
        data1[i]= func2(data1[i])
    return data1
def increment(a):
    return a + 1

def sqr(a):
    return a * a
data = [1, 2, 3, 4]
print(apply_multiple(data, increment, sqr))