import matplotlib.pyplot as plt
import random

def estimate_pi(n):
    count = 0
    estimates = []
    for i in range(1, n+1):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
        if i % 1000 == 0:
            estimates.append(4 * count / i)
    return estimates

estimates = estimate_pi(10000000)
plt.plot(estimates)
plt.axhline(y=3.14159, color='red', linestyle='--')
plt.xlabel('Steps (x1000)')
plt.ylabel('Estimated Pi')
plt.title('Convergence of Pi estimate')
plt.show()