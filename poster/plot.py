from matplotlib import pyplot as plt
import json as js

times = js.load(open('times.js'))
sizes = js.load(open('sizes.js'))

print(times)
print(sizes)

plt.close('all')
fig, ax=plt.subplots(1,1)
ax.plot(sizes, times['pyt'],label='python')
ax.legend()
plt.show()
