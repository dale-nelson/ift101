def swap():
    var1=input("Please give me a value for a variable: ")
    var2=input("Please give me a value for a second variable: ")
    var3=var1
    var1=var2
    var2=var3
    return var1,var2

print(swap())