---

```python
import numpy as np
import matplotlib.pyplot as plt
from math import exp, sqrt

# === Constants and Physical Parameters ===
mass = 6.64e-27        # kg (alpha particle)
V = 25e6               # eV (barrier height)
E = 5e6                # eV (alpha particle energy)
width = 1e-14          # m (barrier width)
hbar = 1.055e-34       # Js
eV_to_J = 1.6e-19      # eV to J

# === Tunneling Probability Calculation ===
def tunneling_probability(mass, V, E, width, hbar):
    V_J = V * eV_to_J
    E_J = E * eV_to_J
    k = sqrt(2 * mass * (V_J - E_J)) / hbar
    return exp(-2 * k * width)

P = tunneling_probability(mass, V, E, width, hbar)
print(f"Tunneling probability per time step: {P:.2e}")

# === Monte Carlo Simulation ===
num_particles = 1000
max_steps = 10000
decay_times = []

for _ in range(num_particles):
    for t in range(max_steps):
        if np.random.rand() < P:
            decay_times.append(t)
            break

# === Visualization ===
plt.figure(figsize=(10, 6))
plt.hist(decay_times, bins=50, color='orange', edgecolor='black')
plt.title("Simulated Alpha Decay Times (Quantum Tunneling)")
plt.xlabel("Time Steps Until Decay")
plt.ylabel("Number of Particles Decayed")
plt.grid(True)
plt.tight_layout()

# Save image for GitHub README
plt.savefig("images/decay_histogram.png")
plt.show()
