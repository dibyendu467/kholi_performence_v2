import numpy as np

# arr=np.array([
#     [1,2,3,4],
#     [4,5,6,8],
#     [7,8,9,2]
# ])
# # print(arr[:2,1:3])
# print(arr[:3,0:2])#last row col0,col1
# print(arr[:1])#second row
# print(arr[:,2:3])#third col
# print(arr[:,0:3])#col1 & col2


#boolean array indexing
# arr=np.array([
#         [1,2,3,4],
#         [4,5,6,8],
#         [7,8,9,2]
# ])
# print(arr)
# bool_idx=[arr>3]# crate boolean array  is grater than 3 in array matrix
# print(bool_idx)
# x=np.array([
#     [2,4],
#     [5,3]
# ])
# print(x)
# y=np.array([
#     [3,4],
#     [2,4]
# ])


# print(y)

# # print(x+y)
# # print(np.add(x,y))
# # print(np.subtract(x,y))
# # print(np.multiply(x,y))
# # print(np.divide(x,y))
# # print(np.sqrt(x))

# v=np.array([6,7])
# w=np.array([8,9])
# print(v.dot(w))
# print(np.dot(v,w))
# print(np.dot(x,w))
# print(x.dot(w))
# print(x.dot(y))
# print(np.dot(x,y))


# # print(x)
# # print(x.T)


# u=np.array([
#     [3,0,5],
#     [6,7,3],
#     [6,8,4]
# ])


# print(u)
# print(u.T)
# print("Sum of all element of u:",np.sum(u))
# print("sum of each column:",np.sum(u,axis=0))
# print("sum of al rows:",np.sum(u,axis=1))

# x=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# v=np.array([1,0,1])

#for loop route

# y=np.empty_like(x)
# print(y)

# for i in range(len(x)):
#     y[i,:] = x[i,:]+v
# print(y)
# print(x)

# stacked_v=np.tile(v,[3,1])
# print(stacked_v)
# print(x+stacked_v)
# print(x+v)

# reshape................................



x=np.array([1,2,3])

print(x)

print(np.reshape(x,(3,1)))

x=np.array([
    [3,4,5],
    [6,2,1]
])
print(x)
print(np.reshape(x,(3,2)))