import copy
def create_operation(op):
    def operation(a,b):
        if(op == "add"):
            return a+b
        if(op == "subtract"):
            return a-b
        if(op == "multiply"):
            return a*b
        if(op == "divide"):
            return a/b
    return operation
#my_func = create_operation("add")
#print(my_func(4, 6))  # Ожидается: 10