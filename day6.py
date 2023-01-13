import numpy as np

# arr=np.array([1,2,4])
# print(arr,type(arr))
# print("Shape of arr:",arr.shape)#shape of the array

# arr = np.array(
#     [
#         [1,3,2],
#         [3,4,5] 
#     ]
# )
# print(arr)
# print("Shape of arr:",arr.shape)
# arr2D=np.array([[1,3,2],[3,4,5],[6,7,7]])
# print(arr2D,arr2D.shape)
# print(type(arr2D))
# print(arr2D.size)
# print(
#     arr2D[0,0],arr2D[0,1],arr2D[0,2]
# )
# print(
#      arr2D[1,0],arr2D[1,1],arr2D[1,2]
# )
# print(
#     arr2D[2,0],arr2D[2,1],arr2D[2,2]
# )
# arr3D=np.array([
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ],
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ],
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ]
# ])
# print(arr3D)
# print(arr3D.shape)
# print(arr3D[0,0,0],arr3D[0,1],arr3D[0])




arr2D=np.array([
        [1,2],
        [2,4],
        [5,6]
])
arr2D[0]=[2,4]
print(arr2D)
zeros=np.zeros([2,4])
print(zeros)

one=np.ones([4,7])
print(one)

constant=np.full((3,3),9)
print(constant)
print(constant.shape)
print(constant.dtype)
random=np.random.random((4,4))
print(random)

