# Geometry: Dynamic Aperture Design

This project explores the geometric optimization of a variable aperture system, inspired by observations of an ethanol stove's flame control mechanism. The goal is to create a safer and more efficient method of controlling combustion through precisely designed geometric patterns.

## Project Overview

Traditional ethanol stoves use a sliding plate mechanism to control the flame, which can be hazardous due to proximity to the heat source. This project proposes an innovative solution: two superimposed plates with specially designed apertures that can be rotated relative to each other. This rotation creates a dynamic opening pattern that transitions from a small central aperture to an expanding ring, allowing precise control over the combustion process.

## Physical Parameters

The system is governed by several key parameters:

- $(x,y)$: Cartesian coordinates
- $(r, \theta)$: Radial coordinates
- $\theta$: Rotation angle (optimal range: 0° to 30°)
- $r_\mathrm{com}$: Center-of-mass radius of the aperture (range: 0 to $r_\mathrm{max}$)
- $A_\mathrm{rel}$: Relative aperture area (target range: 0 to 20%)

The design aims for monotonic growth in both $r_\mathrm{com}$ and $A_\mathrm{rel}$ as the rotation angle increases, ensuring smooth and predictable control over the combustion process.

### Definitions

Let $A_r(\theta)$ be the open area in an annular ring of radius $r$ and radial width $\Delta r$ at rotation angle $\theta$ (units: cm$^2$). In the continuum limit define an area density $a(r,\theta)$ so that

\[A_r(\theta) \approx a(r,\theta)\,\Delta r.\]

Total open area (discrete):

\[A(\theta) = \sum_{r} A_r(\theta) \approx \int_0^{r_{\mathrm{max}}} a(r,\theta)\,dr \quad(\text{units: cm}^2)\]

Relative open area (percent):

\[A_{\mathrm{rel}}(\theta) = 100\cdot \frac{A(\theta)}{\pi r_{\mathrm{max}}^2} \quad(\%)\]

Center-of-mass radius (first moment):

\[r_{\mathrm{com}}(\theta) = \frac{\sum_r r\,A_r(\theta)}{\sum_r A_r(\theta)} \approx \frac{\int_0^{r_{\mathrm{max}}} r\,a(r,\theta)\,dr}{\int_0^{r_{\mathrm{max}}} a(r,\theta)\,dr} \quad(\text{cm})\]

Local open fraction along the circumference (unitless). For an annulus at radius $r$:

\[f(r,\theta) = \frac{A_r(\theta)}{2\pi r\,\Delta r} \in [0,1]\]

This gives the fraction of the ring's circumference that is open at radius $r$ and rotation $\theta$.

Notes:

- The discrete sums assume a radial binning with width $\Delta r$. For accurate measurements use $\Delta r \ll r_{\mathrm{max}}$.
- Continuous forms use the area density $a(r,\theta)$ and integrals over $r \in [0,r_{\mathrm{max}}]$.
- Typical parameter ranges used in this project:
  - $\theta$: 0°–30° (rotation angle)
  - $A_{\mathrm{rel}}$: 0%–20% (relative open area)
  - $r_{\mathrm{com}}$: 0–$r_{\mathrm{max}}$ (cm)

## Current Development Status

While simple geometric solutions like spiral patterns are possible, this project explores more sophisticated approaches:

0. Implementation a stable analysis tool
1. Implementation of 2D grids and monohedral tilings
2. Investigation of Moiré patterns inspired by twisted bilayer graphene
3. Exploration of 2D quasicrystals and Penrose tilings

The current focus is on understanding and implementing quasicrystal patterns, which offer unique geometric properties that could provide optimal aperture control. This investigation has led to deep theoretical study, including detailed analysis of Penrose tiling systems and their applications to this specific problem.
