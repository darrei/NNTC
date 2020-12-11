import json
import os

import matplotlib.pyplot as plt

p = os.path.abspath('flow.json')
with open(p) as f:
    data = json.load(f)
time = list()
Mass_flow_liquid_lc = list()
Mass_flow_gas_lc = list()
Mass_flow_water_lc = list()

for key in data:
    time.append(key)
    Mass_flow_liquid_lc.append(abs(data.get(key)['data']['left_boundary']['Mass_flow_liquid_lc']))
    Mass_flow_gas_lc.append(abs(data.get(key)['data']['left_boundary']['Mass_flow_gas_lc']))
    Mass_flow_water_lc.append(abs(data.get(key)['data']['left_boundary']['Mass_flow_water_lc']))

x = Mass_flow_liquid_lc
y = Mass_flow_gas_lc
z = Mass_flow_water_lc

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(Mass_flow_liquid_lc, Mass_flow_gas_lc, Mass_flow_water_lc, label='parametric curve')

fig, ax = plt.subplots()
ax.plot(time, x, color='#0a0b0c', label='Mass_flow_liquid_lc')
ax.plot(time, y, label='Mass_flow_gas_lc')
ax.plot(time, z, color="darkmagenta", label='Mass_flow_water_lc')
ax.legend(fontsize=10,
          ncol=1,
          facecolor='oldlace',
          edgecolor='r',
          title='Прямые',
          title_fontsize='15'
          )
plt.show()
