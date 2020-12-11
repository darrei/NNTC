import json
import os

import matplotlib.pyplot as plt
import numpy as np

p = os.path.abspath('output.json')
with open(p) as f:
    data = json.load(f)
k = 0
time_short = list()
time = list()
boundary = list()
pressure = list()
s = 0
c_array = list()
my_dict = {
    "left_boundary": 1,
    "1_0": 2,
    "1_1": 3,
    "1_2": 4,
    "2_0": 5,
    "2_1": 6,
    "2_2": 7,
    "3_0": 8,
    "3_1": 9,
    "3_2": 10,
    "right_boundary": 11

}
my_dict_keys = my_dict.keys()
for key in data:
    for i in data.get(key):
        time_short.append(data.get(key)[i]['time'])
        # print(data.get(key)[i]['data'])
        for k in data.get(key)[i]['data']:
            time.append(data.get(key)[i]['time'])
            boundary.append(my_dict[k])

            pressure.append(data.get(key)[i]['data'][k]["pressure"])
            c_array.append((my_dict[k], data.get(key)[i]['data'][k]["pressure"]))

x = time
y = boundary
z = pressure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.tricontourf(x, y, z)
# ax.scatter(x,y,z)
# ax.plot(x,y,z)
ax.set_xlabel("Время")
ax.set_ylabel("Границы")
ax.set_yticks(np.arange(0, 11, step=1))
ax.set_yticklabels(my_dict_keys, rotation=90, fontsize=8)
ax.set_zlabel("Давление")

plt.show()
