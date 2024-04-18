import numpy as np
import random
import matplotlib.pyplot as plt

def measure(phi):
    outcome = random.choices((0, 1), weights = (phi[0]**2, phi[1]**2))
    return outcome[0]

state0 = np.array((1,0))

a = 0
a = float(input("Type a real value: "))
print("Chosen a = {}".format(a))
opU = np.array(((np.cos(a/2), np.sin(a/2)), (-np.sin(a/2), np.cos(a/2))))

phi = np.dot(opU, state0)

measurements = []

for i in range(0, 100):
    measurements.append(measure(phi))

print("Expected values:\nP|0> = {}\nP|1> = {}".format(phi[0]**2, phi[1]**2))
plt.hist(measurements, bins = 2)
plt.show()