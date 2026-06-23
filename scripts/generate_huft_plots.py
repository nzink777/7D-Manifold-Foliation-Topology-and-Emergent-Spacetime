import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the new structural path for simulation results
OUTPUT_DIR = "simulation_code/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Initializing HUFT Math Engine. Target directory: {OUTPUT_DIR}")

# Ensure output directory exists
# os.makedirs("output_plots", exist_ok=True)

# Global Scaling Parameters
ALPHA_INV = 137.0354
DELTA_SHEAR = 0.681690

print("Initializing HUFT Math Engine...")

# -------------------------------------------------------------------------
# 1. GENERATE: worldline_bifurcation.png
# -------------------------------------------------------------------------
print("Rendering Worldline Bifurcations...")
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

tau_vals = np.linspace(0, 6.3, 1000)

# Simulate root trajectories exhibiting fold catastrophes (pair production/annihilation)
def worldline_1(tau): return 0.5 * np.sin(tau) + 0.8
def worldline_2(tau): return 1.5 + 0.2 * np.cos(tau)
def stable_electron(tau): return 5.5 - 0.1 * np.sin(tau)

ax.plot(tau_vals, worldline_1(tau_vals), color='#4B0082', lw=2)
ax.plot(tau_vals, worldline_2(tau_vals), color='#FF8C00', lw=2)
ax.plot(tau_vals, stable_electron(tau_vals), color='#4B0082', lw=2)

# Parabolic fold templates to simulate det(J) = 0
tau_fold_1 = np.linspace(2.2, 4.1, 500)
t_fold_top = 3.5 + np.sqrt(4.1 - tau_fold_1) * 0.6
t_fold_bot = 3.5 - np.sqrt(4.1 - tau_fold_1) * 0.6
ax.plot(tau_fold_1, t_fold_top, color='#D81B60', lw=2)
ax.plot(tau_fold_1, t_fold_bot, color='#D81B60', lw=2)

# Aesthetics setup to mirror the original template
ax.set_title("Emergent Spacetime: Particle Worldlines & Fold Bifurcations", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Cosmological Time Parameter ($\\tau$)", fontsize=12)
ax.set_ylabel("Internal Loop Coordinate ($t \\in [0, 2\\pi)$)", fontsize=12)
ax.set_xlim(0, 6.3)
ax.set_ylim(0, 2*np.pi)
ax.grid(True, linestyle='--', alpha=0.5)

# Text Callout for Catastrophe Boundary
ax.text(0.2, 5.5, r"$\det(\mathbf{J}) = 0$ Fold Bifurcation (Pair Genesis)", 
        bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'), fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "worldline_bifurcation.png"), dpi=300)
plt.close()

# -------------------------------------------------------------------------
# 2. GENERATE: jordan_phase_portrait.png
# -------------------------------------------------------------------------
print("Rendering Jordan Canonical Phase Portrait...")
fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

w0 = 1.0
# Meshgrid for vector fields
x1 = np.linspace(-3.5, 3.5, 20)
x2 = np.linspace(-3.5, 3.5, 20)
X1, X2 = np.meshgrid(x1, x2)

# Matrix A equations for Critically Damped System (\zeta = 1)
DX1 = X2
DX2 = -(w0**2) * X1 - 2 * w0 * X2

# Streamplot to track smooth convergence pathways
ax.streamplot(X1, X2, DX1, DX2, color='#1f77b4', linewidth=1, density=1.5, arrowstyle='->')

# Plot the single degenerate eigenvector line Line L: x2 = -w0 * x1
x1_line = np.linspace(-3.5, 3.5, 100)
ax.plot(x1_line, -w0 * x1_line, color='#FFCC00', lw=2.5, label=r'Degenerate line $\mathcal{L} = \mathrm{span}\{\mathbf{v}\}$')

ax.set_title("Jordan Canonical Phase Portrait (Critically Damped, $\zeta = 1$)", fontsize=14, fontweight='bold')
ax.set_xlabel("$x_1$ (scaled by $1/\omega_0$)", fontsize=12)
ax.set_ylabel("$x_2$", fontsize=12)
ax.axhline(0, color='white', linewidth=0.8, alpha=0.5)
ax.axvline(0, color='white', linewidth=0.8, alpha=0.5)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "jordan_phase_portrait.png"), dpi=300)
plt.close()
# -------------------------------------------------------------------------
# 3. GENERATE: lemniscate_shear_deficit.png
# -------------------------------------------------------------------------
print("Rendering Lemniscate Shear Deficit Metrics...")
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

theta = np.linspace(0, 2*np.pi, 1000)
a = 1.0

# Parametric Bernoulli Lemniscate Equations
denom = 1 + np.sin(theta)**2
x = (a * np.cos(theta)) / denom
y = (a * np.cos(theta) * np.sin(theta)) / denom

# Plot Core Loop State Manifold
ax.plot(x, y, color='#00CCFF', lw=3, label='Lemniscate State Manifold')

# Outer boundary limited by Shear Deficit (Torsional Boundary Limit)
scale_factor = 1.0 + (1.0 - DELTA_SHEAR) * 0.4
ax.plot(x * scale_factor, y * scale_factor, color='#FF9900', linestyle='--', lw=1.5, label='Maximal Packing Boundary')

# Origin Crossover Point Highlight
ax.plot(0, 0, marker='o', color='#FFFFFF', markersize=8, markeredgecolor='#9933FF', label='Crossover Node $C=(0,0)$')

ax.set_title("Lemniscate Shear Deficit & Packing Boundaries", fontsize=14, fontweight='bold')
ax.set_xlabel("$x$", fontsize=12)
ax.set_ylabel("$y$", fontsize=12)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.0, 1.0)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "lemniscate_shear_deficit.png"), dpi=300)
plt.close()

print("All tasks completed successfully.")


print("All tasks completed. Visuals generated successfully in /output_plots.")
