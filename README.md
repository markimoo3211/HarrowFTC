# Quantum Tunneling Simulation: Alpha Decay via Monte Carlo

This project simulates **alpha particle emission** from an unstable atomic nucleus using the concept of **quantum tunneling**. It applies a **Monte Carlo method** to model thousands of decay events over time and visualizes the resulting decay times.

---

## What is Quantum Tunneling?

Quantum tunneling is a phenomenon in quantum physics where particles pass through a potential energy barrier they do not have enough energy to overcome classically. It plays a central role in processes like:

- **Alpha decay** of radioactive nuclei
- **Fusion** in stars
- **Electron transport** in semiconductors

---

## Project Overview

In this simulation:

- An alpha particle is modeled as being trapped inside a potential barrier.
- Each particle has a small probability (derived from the tunneling formula) of escaping at each time step.
- The decay times of 1000 such particles are tracked and visualized as a histogram.
- The result shows a classic **exponential decay curve**, as observed in real nuclear physics.

---

## Physics Behind the Code

We calculate the tunneling probability using this equation:

\[
P = \exp\left(-2 \cdot \text{width} \cdot \sqrt{\frac{2m(V - E)}{\hbar^2}}\right)
\]

Where:
- m is the mass of the alpha particle
- V is the potential barrier height
- E is the alpha particle's energy
- \hbar is the reduced Planck constant
- \text{width} is the thickness of the nuclear barrier

---

## Python Simulation

### Dependencies

```bash
pip install numpy matplotlib
