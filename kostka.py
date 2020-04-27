import numpy as np

np.random.seed(123)
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    
    all_walks.append(random_walk)


print(all_walks)

import matplotlib.pyplot as plt
np_aw = np.array(all_walks)

plt.plot(np_aw)
plt.show()

plt.clf()

np_aw_t = np.transpose(np_aw)

plt.plot(np_aw_t)
plt.show()
