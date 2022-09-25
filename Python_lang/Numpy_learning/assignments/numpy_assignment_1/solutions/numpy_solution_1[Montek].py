###############
# author: Montek
###############

import numpy as np

x = np.arange(2, 11)
y = np.arange(2, 11).reshape(3,3)
print(f"Result without reshaping: \n{x}")
print(f"Result with reshaping: \n{y}")


a = [1, 2, 3, 4]
print("Original array")
print(a)
x = np.asfarray(a)
print(f"Array converted to a float type: \n{x}")


x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [40, 50, 60, 70, 80, 90])
print(f"After append values to the end of the array: \n{x}")

A = np.ones(3)
B = np.ones(3)
print(f"Array A: \n{A}")
print(f"Array B: \n{B}")
print(f"A + B: \n{A+B}")

x = [[30*y + 10*x for x in range(1, 4)] for y in range(3)]
print(f"Array: \n{x}")
print(f"1st row extracted: \n{x[:1]}")
print(f"Last element: \n{x[2][2]}")