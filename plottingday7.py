import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)

# print(x)
# print(y)

# plt.plot(x, y)
# plt.show()

# .............................................................................

# x = np.arange(2, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)

# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.plot(x, y_sin)




# print("I am here")

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()

x_1=np.arange(-20,20,.1)
x_2=np.arange(-20,20,.1)
x_3=np.arange(-20,20,.1)


y_1=list(map(lambda z:z*z, x_1))
y_2=list(map(lambda z:5*(z**2)+6*z+1, x_2))
y_3=list(map(lambda z:1-((z**2)/2), x_3))



plt.plot(x_1, y_1)
plt.plot(x_2, y_2)
plt.plot(x_3, y_3)
plt.subplot(1,3,1)
plt.plot(x_1, y_1)
plt.subplot(1,3,2)
plt.plot(x_2, y_2)
plt.subplot(1,3,3)
plt.plot(x_3, y_3)



plt.show()
