import numpy as np

# initialising variables
# n is number of coils
# b is magnitude of field = |field|
# a is area of coil
n = 1
b = 0.2
a = np.pi * 0.075**2
theta = 25


flux = n * b * a * np.cos(theta)


# print the amount of magnetic flux
print("the magnetic flux is:")
print(flux,"Wb")
