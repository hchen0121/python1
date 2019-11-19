import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

plt.plot(np.random.randn(50).cumsum())
plt.show()


print(3//2)

a = None
print(a is None)

dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.minute)


x = -1
if x < 0:
    print('negative number')
elif x == 0:
    pass
else:
    print('end')
