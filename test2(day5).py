# def multiple(var1,var2):
#     result=var1*var2
#     return result
# res=multiple(4,7)
# print(res)
# multipleX= lambda var1,var2:var1*var2
# print(multipleX(4,6))

tem=56

print("Value of temp before the function:",tem)

def test():
    global tem
    tem=9
    print("value of temp inside the function: ",tem)

test()
print("value of temp after the function:",tem)