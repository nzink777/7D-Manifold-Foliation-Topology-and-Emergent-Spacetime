# Heptagonal Unitary Field Theory (HUFT)
### Quantum Emergence from 7D Manifold Bifurcation Boundaries

An open-source mathematical framework and numerical simulation engine exploring the formal transition from higher-dimensional manifold geometry to observable physical invariants.
## ⚖️ Ontological and Structural Distinction of Graphic Assets

To prevent conceptual overlap, the repository separates its visual assets into two distinct ontological classes: **Global Simulation Fields vs. Isolated Local Blueprints**, and **Minimalist Journal Enclosures vs. Technical Architecture Infographics**. Understanding these structural differences is key to parsing the numerical verifications.

### 1. Worldline Visualizations: Macro-Topology vs. Local Catastrophes

The intersection field $\mathcal{P}(\tau) = \gamma(S^{1}) \cap \mathcal{M}^{4}(\tau)$ yields entirely different visual geometries depending on the scale of observation.

## 🌌 Overview

Within the Heptagonal Unitary Field Theory (HUFT) framework, physical observables such as electric charge and inertial rest mass are not arbitrary scalar fields superimposed onto spacetime. Instead, they emerge naturally as intrinsic topological properties of the intersection operator:

$$\mathcal{P}(\tau) = \gamma(S^{1}) \cap \mathcal{M}^{4}(\tau)$$

at or near the fold bifurcation boundaries where the metric Jacobian determinant vanishes ($\det(\mathbf{J}) = 0$).

---

## 🧬 Core Mathematical Formulations

### 1. Quantized Charge as a Topological Orientation Index
Electric charge $Q_{k}$ associated with a discrete localized root path $t_{k}(\tau)$ is formally defined as the topological orientation index (Brouwer degree) of the intersection between the closed 1-manifold loop $\gamma(S^{1}) \hookrightarrow T^{7}$ and the translating 4D macroscopic foliation plane $\mathcal{M}^{4}(\tau)$. 

The quantized charge assignment is governed by the sign of the determinant of the coordinate mapping Jacobian:

$$Q_{k} = \text{sgn}(\det(\mathbf{J})) = \text{sgn}\left(\frac{\partial\mathcal{M}^{4}(\tau)}{\partial t}\right)$$

This orientation index yields strict binary quantization for standard intersections:
* **Matter States:** $Q_{k} = +1$ (Positive orientation crossing)
* **Antimatter States:** $Q_{k} = -1$ (Inverse orientation crossing)

At the exact vertex of pair genesis or annihilation, the slicing family becomes perfectly tangent to the 7D bulk loop, yielding the boundary condition:

$$\det(\mathbf{J}) = 0$$

As the slicing family continues its translation across cosmological time $\tau$, the total index is strictly conserved:

$$\sum Q_{k} = (+1) + (-1) = 0$$

### 2. Inertial Rest Mass as Localized Resonant Tension
Inertial rest mass $M_{k}$ represents the localized geometric tension required to maintain the stability of the knot strands within the moving 4D foliation slice. The emergent rest mass is derived as a function of the discrete integer winding vectors $\omega_{A}$ along the seven toroidal dimensions:

$$M_{k} = \left(\sum_{A=1}^{7}\omega_{A}^{2}\right)^{1/2} \cdot \exp\left(-\frac{1}{\alpha \cdot \delta_{\text{shear}}}\right)$$

Where:
* $\omega_{A} \in \mathbb{Z}$ represents the topological winding numbers ensuring harmonic loop closure under the global congruence:
  $$\sum_{A=1}^{7}\omega_{A} \equiv 0 \pmod 7$$
* $\alpha^{-1} \approx 137.0354$ acts as the global foliation resonance scale.
* $\delta_{\text{shear}} \approx 0.681690$ governs the torsional shear deficit boundary limit.

---

## 📂 Repository Architecture

The repository isolates primary manuscript text, simulation routines, and automatically generated graphic assets into a strict modular directory layout:

```text
├── .github/
│   └── workflows/
│       └── generate_graphs.yml      # CI/CD pipeline for automated plot generation
├── scripts/
│   └── generate_huft_plots.py       # Core Python math & numerical plotting engine
├── simulation_code/
│   └── results/                     # Target directory for automated simulation outputs
│       ├── worldline_bifurcation.png
│       ├── jordan_phase_portrait.png
│       └── lemniscate_shear_deficit.png
├── docs/
│   └── lemniscate_shear.png         # Technical architecture blueprint infographic
└── 7D_Manifold_Foliation_Topology_and_Emergent_Spacetime.tex

