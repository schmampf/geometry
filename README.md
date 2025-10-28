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
$A_\theta$: is the transparent area of the two apertures at fixed rotation angle $\theta$ in cm$^2$

$A_\theta(r)$: is the area within ring at r with width dr in units of cm

$\rangle A\langle_r(\theta)$: the total area, depending on the roation angle

$A_\mathrm{rel} = A(r)$

## Current Development Status

While simple geometric solutions like spiral patterns are possible, this project explores more sophisticated approaches:

1. Implementation of 2D grids and monohedral tilings
2. Investigation of Moiré patterns inspired by twisted bilayer graphene
3. Exploration of 2D quasicrystals and Penrose tilings

The current focus is on understanding and implementing quasicrystal patterns, which offer unique geometric properties that could provide optimal aperture control. This investigation has led to deep theoretical study, including detailed analysis of Penrose tiling systems and their applications to this specific problem.